from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('create_product/', views.createProduct, name='create_product'),


]