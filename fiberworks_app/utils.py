# Import necessary modules
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
import boto3


def optimize_image(image):
    print("Opening the image...")
    img = Image.open(image)
    
    print("Converting the image to RGB...")
    img = img.convert('RGB')
    
    print("Resizing the image...")
    img = img.resize((800, 600), Image.LANCZOS)
    
    img_io = BytesIO()
    
    print("Saving the image to BytesIO buffer...")
    img.save(img_io, 'JPEG', quality=30)
    
    img_file = ContentFile(img_io.getvalue())
    
    print("Optimization complete. Returning the optimized image.")
    return img_file




def delete_image_from_s3(image_key):
    s3 = boto3.client('s3')
    bucket_name = 'your-bucket-name'

    try:
        s3.delete_object(Bucket=bucket_name, Key=image_key)
    except Exception as e:
        # Handle any errors, e.g., object not found, permissions issues, etc.
        print(f"Failed to delete object from S3: {e}")