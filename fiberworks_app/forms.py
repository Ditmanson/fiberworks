from django.forms import ModelForm
from .models import *

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'
class HomeScreenForm(ModelForm):
    class Meta:
        model = Homescreen
        fields = '__all__'