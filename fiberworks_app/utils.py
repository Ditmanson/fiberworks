# Import necessary modules
from PIL import Image, ExifTags
from io import BytesIO
from django.core.files.base import File
import boto3
from django.conf import settings


def compress_image(image):
    img = Image.open(image)

    # Correct the orientation of the image
    try:
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                break
        exif = dict(img._getexif().items())

        if exif[orientation] == 3:
            img = img.transpose(Image.ROTATE_180)
        elif exif[orientation] == 6:
            img = img.transpose(Image.ROTATE_270)
        elif exif[orientation] == 8:
            img = img.transpose(Image.ROTATE_90)
    except (AttributeError, KeyError, IndexError):
        # Cases: image don't have getexif
        pass

    img_io = BytesIO()
    img.save(img_io, format='JPEG', quality=15, optimize=True)

    # Create a django file object
    django_file = File(img_io, name=image.name)

    return django_file


def delete_image_from_s3(image_key):
    s3 = boto3.client('s3', 
                      aws_access_key_id=settings.AWS_ACCESS_KEY_ID, 
                      aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
    bucket_name = 'jades-fiberworks-bucket'

    try:
        s3.delete_object(Bucket=bucket_name, Key=image_key)
    except Exception as e:
        # Handle any errors, e.g., object not found, permissions issues, etc.
        print(f"Failed to delete object from S3: {e}")