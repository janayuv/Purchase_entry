# supplier/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.supplier_list, name='supplier_list'),
    path('add/', views.supplier_add, name='supplier_add'),
    path('<int:id>/update/', views.supplier_update, name='supplier_update'),
    path('<int:id>/delete/', views.supplier_delete, name='supplier_delete'),
]
