from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.ProductListView.as_view(), name='products'),
    path('dashboard/', views.products, name='dashboard'),
    path('update_product/<str:pk>/', views.updateProduct, name='update_product'),
    path('create_product/', views.createProduct, name='create_product'),
    path('delete_product/<str:pk>/', views.deleteProduct, name='delete_product'),
    path('product_details/<str:pk>/', views.ProductDetailView.as_view(), name='product_details'),
    path('customer_login', views.customerLogin, name='customer_login'),
]
