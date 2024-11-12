# supplier/forms.py

from django import forms
from .models import Supplier

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'gst_no', 'tds_applicable', 'contact', 'email']
