from django.urls import path
from .views import *

urlpatterns = [
    path('clientes/', ClienteListView.as_view()),
    path('clientes/nuevo/', ClienteCreateView.as_view()),
    path('facturas/', FacturaListView.as_view()),
    path('facturas/nuevo/', FacturaCreateView.as_view()),
]