from django.views.generic import ListView, CreateView
from .models import Cliente, Factura

class ClienteListView(ListView):
    model = Cliente
    template_name = 'clientes/list.html'

class ClienteCreateView(CreateView):
    model = Cliente
    fields = ['nombre', 'documento']
    success_url = '/clientes/'


class FacturaListView(ListView):
    model = Factura
    template_name = 'facturas/list.html'

class FacturaCreateView(CreateView):
    model = Factura
    fields = ['numero', 'fecha', 'monto', 'cliente']
    success_url = '/facturas/'