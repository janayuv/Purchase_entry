# supplier/admin.py

from django.contrib import admin
from .models import Supplier

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'gst_no', 'tds_applicable', 'contact', 'email')
    search_fields = ('name', 'gst_no', 'contact', 'email')
    list_filter = ('tds_applicable',)

    # Optional: Fields that show as clickable links in the admin list view
    list_display_links = ('name', 'gst_no')

    # Optional: Make fields editable directly in the list display
    list_editable = ('tds_applicable', 'contact', 'email')
