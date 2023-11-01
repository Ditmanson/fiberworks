from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('update_product/<str:pk>/', views.updateProduct, name='update_product'),
    path('update_tag/<str:pk>/', views.updateTag, name='update_tag'),
    path('create_product/', views.createProduct, name='create_product'),
    path('create_tag/', views.createTag, name='create_tag'),
    path('delete_product/<str:pk>/', views.deleteProduct, name='delete_product'),
    path('delete_tag/<str:pk>/', views.deleteTag, name='delete_tag'),
    path('product_details/<str:pk>/', views.ProductDetailView.as_view(), name='product_details'),
    path('customer_login', views.customerLogin, name='customer_login'),
]
