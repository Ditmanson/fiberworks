from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
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
class CreateUserFrom(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']