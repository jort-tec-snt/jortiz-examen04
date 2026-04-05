from django.db import models

#Creando el modelo
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    documento = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Factura(models.Model):
    numero = models.CharField(max_length=20)
    fecha = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.numero
