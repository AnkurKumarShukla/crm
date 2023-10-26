from django.contrib import admin
from django.urls import path
# from django.http import HttpResponse
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('product/', views.product,name='product'),
    path('customer/<str:pk_text>/', views.customer,name ='customer'),
    path('create_order/', views.create_order,name ='create_order'),
    

]