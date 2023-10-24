from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.views.generic import *
from .forms import *

class ProductListView(ListView):
    model = Product
    template_name = 'fiberworks_app/products.html'
    context_object_name = 'products_in_stock'
    ordering = ['name']
    paginate_by = 10

class ProductDetailView(DetailView):
    model = Product
    template_name = 'fiberworks_app/product_details.html'
    context_object_name = 'product'

def createProduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the product to the database
            return redirect('create_product')  # Redirect to an empty form

    else:
        form = ProductForm()  # Create a new form for GET requests

    context = {'form': form}
    return render(request, 'fiberworks_app/product_form.html', context)

def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()  # Save the product to the database
            return redirect('product_details', pk=product.id)  # Redirect to the product details page

    context = {'form': form}
    return render(request, 'fiberworks_app/product_form.html', context)

def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('dashboard')

    context = {'product': product}
    return render(request, 'fiberworks_app/delete_product.html', context)

def index(request):
    products_in_stock = Product.objects.filter(in_stock=True)
    return render(request, 'fiberworks_app/index.html', {'products_in_stock': products_in_stock})

def products(request):
    products = Product.objects.all()
    return render(request, 'fiberworks_app/dashboard.html', {'products': products})

def customerLogin(request):
    customer = Customer.objects.all()
    return render(request, 'fiberworks_app/customer_login.html', {'customer': customer})
