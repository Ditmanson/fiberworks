from django.forms import ModelForm, CheckboxSelectMultiple 
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'image': forms.FileInput(attrs={'id': 'image-upload','class': 'form-control btn btn-light' }),
            'tags': forms.CheckboxSelectMultiple(),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'in_stock': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'on_homepage': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            # other fields...
        }

class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'

class HomeScreenForm(ModelForm):
    class Meta:
        model = Homescreen
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'paragraph': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CreateUserFrom(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']