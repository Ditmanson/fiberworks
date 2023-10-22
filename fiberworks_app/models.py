from django.db import models
from django.urls import reverse

class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
    
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
    description = models.CharField(max_length=250, blank=True, null=True)
    category = models.CharField(max_length=20, default='hats', choices=CATEGORY)
    tags = models.ManyToManyField(Tag)
    in_stock = models.BooleanField(default=False)    
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=250, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    #image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})


    

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
        return self.product.name
    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
