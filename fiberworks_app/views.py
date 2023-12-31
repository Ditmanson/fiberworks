from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.views.generic import *
from .forms import *
from .utils import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.apps import apps
from django.shortcuts import get_object_or_404


def index(request):
    homescreen = Homescreen.objects.all()
    home_page_products = Product.objects.filter(on_homepage=True)
    products = Product.objects.all()
    return render(request, 'fiberworks_app/index.html', {'home_page_products': home_page_products, 'homescreen': homescreen, 'products': products })

@login_required(login_url='login')
def dashboard(request):
    products = Product.objects.all()
    tags = Tag.objects.all().distinct()
    homescreen = Homescreen.objects.all()
    return render(request, 'fiberworks_app/dashboard.html', {'products': products, 'tags': tags, 'homescreen': homescreen})

@login_required(login_url='login')  
def deleteHomeScreen(request, pk):
    homescreen = Homescreen.objects.get(id=pk)
    if request.method == 'POST':
        homescreen.delete()
        return redirect('index')

    context = {'homescreen': homescreen}
    return render(request, 'fiberworks_app/delete_home_screen.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'fiberworks_app/product_details.html'
    context_object_name = 'product'

@login_required(login_url='login')
def createProduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.image = compress_image(product.image)  # Compress the image before saving
            product.save()  # Save the product to the database
            return redirect('index')  # Redirect to an empty form

    else:
        form = ProductForm()  # Create a new form for GET requests

    context = {'form': form}
    return render(request, 'fiberworks_app/product_form.html', context)

@login_required(login_url='login')
def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()  # Save the product to the database
            return redirect('index')  # Redirect to the product details page

    context = {'form': form}
    return render(request, 'fiberworks_app/product_form.html', context)

@login_required(login_url='login')
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    # Get the S3 image key from the product
    image_key = product.image.name if product.image else None
    if request.method == 'POST':
        # Delete the product
        product.delete()
        # Delete the associated image from the S3 bucket
        if image_key:
            delete_image_from_s3(image_key)
        return redirect('index')
    context = {'product': product,
               'object_id': product.pk,
                'delete_url': reverse('delete_product', args=[pk]),
               }
    return render(request, 'fiberworks_app/delete_product.html', context)


def products(request):
    products = Product.objects.filter(in_stock=True)
    homescreen = Homescreen.objects.all()
    return render(request, 'fiberworks_app/products.html', {'products': products, 'homescreen': homescreen})

@login_required(login_url='login')
def createTag(request):
    if request.method == 'POST':
        form = HomeScreenForm(request.POST)
        if form.is_valid():
            form.save()  # Save the product to the database
            return redirect('index')  # Redirect to an empty form
    else:
        form = TagForm()  # Create a new form for GET requests
    context = {'form': form}
    return render(request, 'fiberworks_app/Tag_form.html', context) 

@login_required(login_url='login')
def updateTag(request, pk):
    tag = Tag.objects.get(id=pk)
    form = TagForm(instance=tag)
    if request.method == 'POST':
        form = TagForm(request.POST,  instance=tag)
        if form.is_valid():
            form.save()  # Save the product to the database
            return redirect('index')  # Redirect to the product details page

    context = {'form': form}
    return render(request, 'fiberworks_app/home_screen_form.html', context)

@login_required(login_url='login')
def deleteTag(request, pk):
    tag = Tag.objects.get(id=pk)
    if request.method == 'POST':
        tag.delete()
        return redirect('index')

    context = {'tag': tag,
            'object_id': tag.pk,
            'delete_url': reverse('delete_tag', args=[pk]), 
               }
    return render(request, 'fiberworks_app/delete_product.html', context)

@login_required(login_url='login')
def createHomeScreen(request):
    if request.method == 'POST':
        form = HomeScreenForm(request.POST)
        if form.is_valid():
            form.save()  # Save the product to the database
            return redirect('index')  # Redirect to an empty form
    else:
        form = HomeScreenForm()  # Create a new form for GET requests
    context = {'form': form}
    return render(request, 'fiberworks_app/home_screen_form.html', context)

@login_required(login_url='login')
def updateHomeScreen(request, pk):
    homescreen = Homescreen.objects.get(id=pk)
    form = HomeScreenForm(instance=homescreen)
    if request.method == 'POST':
        form = HomeScreenForm(request.POST,  instance=homescreen)
        if form.is_valid():
            form.save()  # Save the product to the database
            return redirect('index')  # Redirect to the product details page

    context = {'form': form}
    return render(request, 'fiberworks_app/home_screen_form.html', context)

def homescreen(request):
    homescreen = Homescreen.objects.all()
    return render(request, 'fiberworks_app/homescreen.html', {'homescreen': homescreen})


def Register(request):
    if request.user.is_authenticated:
        return redirect('products')
    else:
        form = CreateUserFrom()
        if request.method == 'POST':
            form = CreateUserFrom(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')  # Redirect to the login page
        context = {'form': form}
        return render(request, 'fiberworks_app/register.html', context)


def Login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('index')
                else:
                    messages.info(request, 'Username OR password is incorrect')
        else:
            form = AuthenticationForm()
        return render(request, 'fiberworks_app/login.html', {'form': form})

def Logout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def generic_delete(request, model_name, pk):
    ModelClass = apps.get_model('fiberworks_app', model_name)
    instance = get_object_or_404(ModelClass, pk=pk)

    if request.method == 'POST':
        # Get the S3 image key from the instance if it has an image attribute
        image_key = instance.image.name if hasattr(instance, 'image') and instance.image else None
        # Delete the instance
        instance.delete()
        # Delete the associated image from the S3 bucket
        if image_key:
            delete_image_from_s3(image_key)
        return redirect('index')

    context = {
        'object': instance,
        'delete_url': reverse('generic_delete', args=[model_name, pk]),
    }
    return render(request, 'fiberworks_app/delete_object.html', context)