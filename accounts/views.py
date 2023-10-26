from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
from forms import OrderForm


def home(request):
    orders=Order.objects.all()
    customer=Customer.objects.all()
    total_customer= customer.count()
    total_order=orders.count()
    
    delivered=orders.filter(status='Delivered').count()
    pending=orders.filter(status='Pending').count()



    context={'orders':orders,'customer':customer,'total_customer':total_customer,'total_order':total_order,'delivered':delivered,'pending':pending}


    





    return render(request, 'accounts/dashboard.html',context)

def product(request):
    products= Product.objects.all()
    return render(request, 'accounts/products.html',{'products':products})
def customer(request,pk_text):
    customer= Customer.objects.get(id=pk_text)
    orders= customer.order_set.all()
    order=orders.count()

    context={'customer':customer,'orders':orders,'order':order}
    return render(request, 'accounts/customer.html',context)



def create_order(request):
    



    context={}
    return render(request,'accounts/order_form.html',context)