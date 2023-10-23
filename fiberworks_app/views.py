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
    template_name = 'fiberworks_app/product_detail.html'
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


def index(request):
    products_in_stock = Product.objects.filter(in_stock=True)
    return render(request, 'fiberworks_app/index.html', {'products_in_stock': products_in_stock})

def products(request):
    products_in_stock = Product.objects.filter(in_stock=True)
    return render(request, 'fiberworks_app/products.html', {'products_in_stock': products_in_stock})

# Create your views here.
# def index(request):
#     student_active_portfolios = Student.objects.select_related('portfolio').all().filter(portfolio__is_active=True)
#     print("active portfolio query set", student_active_portfolios)
#     return render( request, 'portfolio_app/index.html', {'student_active_portfolios':student_active_portfolios})