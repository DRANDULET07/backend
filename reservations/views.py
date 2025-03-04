# filepath: reservations/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Reservation
from customers.models import Customer
from Tables.models import Table

def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservations/reservation_list.html', {'reservations': reservations})

def reservation_detail(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    return render(request, 'reservations/reservation_detail.html', {'reservation': reservation})

def reservation_create(request):
    if request.method == 'POST':
        customer_id = request.POST.get('customer')
        table_id = request.POST.get('table')
        date = request.POST.get('date')
        status = request.POST.get('status')
        try:
            customer = get_object_or_404(Customer, id=customer_id)
            table = get_object_or_404(Table, id=table_id)
            reservation = Reservation.objects.create(customer=customer, table=table, date=date, status=status)
            return redirect('reservation_detail', id=reservation.id)
        except Customer.DoesNotExist:
            return render(request, 'reservations/reservation_form.html', {'error': 'Customer not found', 'customers': Customer.objects.all(), 'tables': Table.objects.filter(is_available=True)})
        except Table.DoesNotExist:
            return render(request, 'reservations/reservation_form.html', {'error': 'Table not found', 'customers': Customer.objects.all(), 'tables': Table.objects.filter(is_available=True)})
    return render(request, 'reservations/reservation_form.html', {'customers': Customer.objects.all(), 'tables': Table.objects.filter(is_available(True))})

def reservation_update(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    if request.method == 'POST':
        reservation.status = request.POST.get('status', reservation.status)
        reservation.save()
        return redirect('reservation_detail', id=reservation.id)
    return render(request, 'reservations/reservation_form.html', {'reservation': reservation})

def reservation_delete(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    if request.method == 'POST':
        reservation.delete()
        return redirect('reservation_list')
    return render(request, 'reservations/reservation_confirm_delete.html', {'reservation': reservation})