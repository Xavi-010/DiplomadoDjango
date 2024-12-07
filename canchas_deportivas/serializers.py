from rest_framework import serializers
from .models import Categoria
from .models import Cancha
from .validators import validar_nombre

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class CanchaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cancha
        fields = '__all__'

class ReporteCanchasSerializer(serializers.Serializer):
    cantidad = serializers.IntegerField()
    canchas = CanchaSerializer(many=True)

class ContactSerializer(serializers.Serializer):
    name = serializers.CharField(validators=[validar_nombre])
    email = serializers.EmailField()
    message = serializers.CharField()