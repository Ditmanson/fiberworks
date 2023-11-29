from django.urls import path
from . import views 

urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    path('homescreen', views.homescreen, name='homescreen'),
    path('create_home_screen/', views.createHomeScreen, name='create_home_screen'),
    path('update_home_screen/<str:pk>/', views.updateHomeScreen, name='update_home_screen'),
    # path('delete_home_screen/<str:pk>/', views.deleteHomeScreen, name='delete_home_screen'),

    #producds
    path('products/', views.products, name='products'),
    path('product_details/<str:pk>/', views.ProductDetailView.as_view(), name='product_details'),
    path('create_product/', views.createProduct, name='create_product'),
    path('update_product/<str:pk>/', views.updateProduct, name='update_product'),
    # path('delete_product/<str:pk>/', views.deleteProduct, name='delete_product'),

    #tags
    path('create_tag/', views.createTag, name='create_tag'),
    path('update_tag/<str:pk>/', views.updateTag, name='update_tag'),
    # path('delete_tag/<str:pk>/', views.deleteTag, name='delete_tag'),

    #Other URLs
    path('dashboard/', views.dashboard, name='dashboard'),

    #User login and authentication
    path('register', views.Register, name='register'),
    path('login', views.Login, name='login'),
    path('logout', views.Logout, name='logout'),

    #Generic Delete
    path('delete/<str:model_name>/<str:pk>/', views.generic_delete, name='generic_delete'),
    ]
