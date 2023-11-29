from django.db import models
from django.urls import reverse
from .utils import delete_image_from_s3
# from django.core.exceptions import ValidationError
# from PIL import Image, ImageOps
# from django.core.files.images import ImageFile
# import io


class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("tag_detail", kwargs={"pk": self.pk})
    
class Product(models.Model):
    CATEGORY = (
        ('hats', 'hats'),
        ('shawls', 'shawls'),
        ('blankets', 'blankets'),
        ('scarves', 'scarves'),
        ('other', 'other'),
    )
    
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(max_length=2000, blank=True, null=True)
    category = models.CharField(max_length=20, default='hats', choices=CATEGORY)
    tags = models.ManyToManyField(Tag, blank=True)
    image = models.ImageField(upload_to='images/')
    in_stock = models.BooleanField(default=False)    
    on_homepage = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    def delete(self, *args, **kwargs):
    # Delete the image from S3 before deleting the product instance
        if self.image and hasattr(self.image, 'name'):
            delete_image_from_s3(self.image.name)
        super().delete(*args, **kwargs)
    def get_absolute_url(self):
        return reverse("product_details", kwargs={"pk": self.pk})

class Homescreen(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    paragraph = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.title
    # def get_absolute_url(self):
    #     return reverse("homescreen_details", kwargs={"pk": self.pk})


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=250, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    #image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("customer_details", kwargs={"pk": self.pk})


    

class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_ordered = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS, default='Pending')
    def __str__(self):
        return self.product.name if self.product else ''
    def get_absolute_url(self):
        return reverse("order_detail", kwargs={"pk": self.pk})
