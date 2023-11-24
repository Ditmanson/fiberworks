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
from PIL import Image
from io import BytesIO
from django.core.files import File

def index(request):
    products_in_stock = Product.objects.filter(in_stock=True)
    homescreen = Homescreen.objects.all()
    home_page_products = Product.objects.filter(on_homepage=True)
    return render(request, 'fiberworks_app/index.html', {'home_page_products': home_page_products, 'homescreen': homescreen })

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
        return redirect('dashboard')

    context = {'homescreen': homescreen}
    return render(request, 'fiberworks_app/delete_home_screen.html', context)


# class ProductListView(ListView):
#     model = Product
#     template_name = 'fiberworks_app/products.html'
#     context_object_name = 'products_in_stock'
#     ordering = ['name']
#     paginate_by = 10

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
            return redirect('dashboard')  # Redirect to an empty form

    else:
        form = ProductForm()  # Create a new form for GET requests

    context = {'form': form}
    return render(request, 'fiberworks_app/product_form.html', context)

# @
def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()  # Save the product to the database
            return redirect('dashboard')  # Redirect to the product details page

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
        return redirect('dashboard')
    context = {'product': product}
    return render(request, 'fiberworks_app/delete_product.html', context)


def products(request):
    products = Product.objects.filter(in_stock=True)
    return render(request, 'fiberworks_app/products.html', {'products': products, })

@login_required(login_url='login')
def createTag(request):
    if request.method == 'POST':
        form = HomeScreenForm(request.POST)
        if form.is_valid():
            form.save()  # Save the product to the database
            return redirect('dashboard')  # Redirect to an empty form
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
            return redirect('dashboard')  # Redirect to the product details page

    context = {'form': form}
    return render(request, 'fiberworks_app/home_screen_form.html', context)

@login_required(login_url='login')
def deleteTag(request, pk):
    tag = Tag.objects.get(id=pk)
    if request.method == 'POST':
        tag.delete()
        return redirect('dashboard')

    context = {'tag': tag}
    return render(request, 'fiberworks_app/delete_tag.html', context)

@login_required(login_url='login')
def createHomeScreen(request):
    if request.method == 'POST':
        form = HomeScreenForm(request.POST)
        if form.is_valid():
            form.save()  # Save the product to the database
            return redirect('dashboard')  # Redirect to an empty form
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
            return redirect('dashboard')  # Redirect to the product details page

    context = {'form': form}
    return render(request, 'fiberworks_app/home_screen_form.html', context)

def homescreen(request):
    homescreen = Homescreen.objects.all()
    return render(request, 'fiberworks_app/homescreen.html', {'homescreen': homescreen})


def Register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
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
                    return redirect('dashboard')
                else:
                    messages.info(request, 'Username OR password is incorrect')
        else:
            form = AuthenticationForm()
        return render(request, 'fiberworks_app/login.html', {'form': form})

def Logout(request):
    logout(request)
    return redirect('login')
