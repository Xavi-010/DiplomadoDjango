from django.db import models
from .validators import validar_par,validar_longitud_nombre

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.nombre

class Cancha(models.Model):
    nombre = models.CharField(max_length=100,unique=True,validators=[validar_longitud_nombre,])
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    ubicacion = models.TextField()
    descripcion = models.TextField()
    # precio_hora = models.DecimalField(max_digits=10, decimal_places=2) 
    precio_hora_regular = models.DecimalField(max_digits=10, decimal_places=2, default=0.00,validators=[validar_par,])
    precio_hora_nocturno = models.DecimalField(max_digits=10, decimal_places=2, default=0.00,validators=[validar_par,])
    tipo_superficie = models.CharField(max_length=50, choices=[('Césped Natural', 'Césped Natural'),('Césped Artificial', 'Césped Artificial'), ('Concreto', 'Concreto'), ('Arena', 'Arena')])
    disponible = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
    
class Reserva(models.Model):
    nombre_cliente = models.CharField(max_length=100,unique=True,validators=[validar_longitud_nombre])
    total_costo = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    fecha = models.DateField(auto_now_add=True)
    estado =models.BooleanField(default=True)

class DetalleReserva(models.Model):
    cancha = models.ForeignKey(Cancha,on_delete=models.CASCADE)
    reserva = models.ForeignKey(Reserva,on_delete=models.CASCADE)
    cantidad_horas = models.PositiveIntegerField(default=1)
    precio_por_hora = models.DecimalField(max_digits=10,decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, blank=True)

    def save(self, *args, **kwargs):
        self.subtotal = self.cantidad_horas * self.precio_por_hora
        super().save(*args, **kwargs) 
    
