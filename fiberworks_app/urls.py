from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('create_product/', views.createProduct, name='create_product'),
    path('update_product/<str:pk>/', views.updateProduct, name='update_product'),
    path('delete_product/<str:pk>/', views.deleteProduct, name='delete_product'),
    path('product_details/<str:pk>/', views.ProductDetailView.as_view(), name='product_details'),

]
