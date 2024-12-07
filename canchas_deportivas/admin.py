from django.contrib import admin
from .models import Categoria
from .models import Cancha
# Register your models here.


# CATEGORIA
admin.site.register(Categoria)

#PRODUCTO
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre','categoria','precio_hora_regular','ubicacion','tipo_superficie','disponible')
    ordering = ['precio_hora_regular']
    search_fields = ['nombre']
    list_filter = ('disponible','categoria',)

admin.site.register(Cancha,ProductoAdmin)



