from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def index(request):
    products_in_stock = Product.objects.filter(in_stock=True)
    return render(request, 'fiberworks_app/index.html', {'products_in_stock': products_in_stock})

# Create your views here.
# def index(request):
#     student_active_portfolios = Student.objects.select_related('portfolio').all().filter(portfolio__is_active=True)
#     print("active portfolio query set", student_active_portfolios)
#     return render( request, 'portfolio_app/index.html', {'student_active_portfolios':student_active_portfolios})