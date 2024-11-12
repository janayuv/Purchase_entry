# supplier/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Supplier
from .forms import SupplierForm

def supplier_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        suppliers = Supplier.objects.filter(name__icontains=search_query)
    else:
        suppliers = Supplier.objects.all()
    return render(request, 'supplier/supplier_list.html', {'suppliers': suppliers})

def supplier_add(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supplier_list')
    else:
        form = SupplierForm()
    return render(request, 'supplier/supplier_form.html', {'form': form})

def supplier_update(request, id):
    supplier = get_object_or_404(Supplier, pk=id)  # Get supplier by ID or show 404 if not found
    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)  # Bind form with the existing supplier data
        if form.is_valid():
            form.save()  # Save the updated supplier data
            return redirect('supplier_list')  # Redirect to the list of suppliers after saving
    else:
        form = SupplierForm(instance=supplier)  # Pre-fill the form with existing supplier data
    
    return render(request, 'supplier/supplier_form.html', {'form': form, 'supplier': supplier})

def supplier_delete(request, id):
    supplier = get_object_or_404(Supplier, id=id)
    supplier.delete()
    return redirect('supplier_list')
