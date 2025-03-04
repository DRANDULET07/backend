# filepath: customers/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customers/customer_list.html', {'customers': customers})

def customer_detail(request, id):
    customer = get_object_or_404(Customer, id=id)
    return render(request, 'customers/customer_detail.html', {'customer': customer})

def customer_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        customer = Customer.objects.create(name=name, phone=phone)
        return redirect('customer_detail', id=customer.id)
    return render(request, 'customers/customer_form.html')

def customer_update(request, id):
    customer = get_object_or_404(Customer, id=id)
    if request.method == 'POST':
        customer.name = request.POST.get('name', customer.name)
        customer.phone = request.POST.get('phone', customer.phone)
        customer.save()
        return redirect('customer_detail', id=customer.id)
    return render(request, 'customers/customer_form.html', {'customer': customer})

def customer_delete(request, id):
    customer = get_object_or_404(Customer, id=id)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    return render(request, 'customers/customer_confirm_delete.html', {'customer': customer})

def home(request):
    return render(request, 'home.html')