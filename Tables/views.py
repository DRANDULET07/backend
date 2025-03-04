# filepath: Tables/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Table

def table_list(request):
    tables = Table.objects.all()
    return render(request, 'Tables/table_list.html', {'tables': tables})

def table_detail(request, id):
    table = get_object_or_404(Table, id=id)
    return render(request, 'Tables/table_detail.html', {'table': table})

def table_create(request):
    if request.method == 'POST':
        number = request.POST.get('number')
        seats = request.POST.get('seats')
        is_available = request.POST.get('is_available') == 'on'
        table = Table.objects.create(number=number, seats=seats, is_available=is_available)
        return redirect('table_detail', id=table.id)
    return render(request, 'Tables/table_form.html')

def table_update(request, id):
    table = get_object_or_404(Table, id=id)
    if request.method == 'POST':
        table.number = request.POST.get('number', table.number)
        table.seats = request.POST.get('seats', table.seats)
        table.is_available = request.POST.get('is_available') == 'on'
        table.save()
        return redirect('table_detail', id=table.id)
    return render(request, 'Tables/table_form.html', {'table': table})

def table_delete(request, id):
    table = get_object_or_404(Table, id=id)
    if request.method == 'POST':
        table.delete()
        return redirect('table_list')
    return render(request, 'Tables/table_confirm_delete.html', {'table': table})