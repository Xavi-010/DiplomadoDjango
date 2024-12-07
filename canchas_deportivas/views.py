from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.shortcuts import get_object_or_404
from .models import Categoria
from .models import Cancha
from .forms import CanchaForm
from rest_framework import viewsets,generics
from .serializers import CategoriaSerializer
from rest_framework.decorators import api_view
from .serializers import CanchaSerializer,ReporteCanchasSerializer,ContactSerializer


# Create your views here.

def index(request):
    return HttpResponse('hola mundo')

def contact(request,name):
    return HttpResponse(f"Bienvenido a Django {name}")

# def categorias(request):
#     categorias = Categoria.objects.all()
#     return render(request,'categorias.html',{
#         'categorias':categorias
#     })

def categorias(request):
    post_nombre = request.POST.get("nombre", "")
    if post_nombre:
        q = Categoria(nombre=post_nombre)
        q.save()
        # categorias = Categoria.objects.filter(nombre__icontains=nombre)
    categorias = Categoria.objects.all()
    return render(request, "form_categorias.html", {
        "categorias": categorias
    })

# def canchaFormView(request):
#     form = CanchaForm(request.POST)
#     if form.is_valid():
#         form.save()
#     return render(request, 'form_canchas.html', {'form':form})


def canchaFormView(request):
    form = CanchaForm()
    cancha = None
    id_cancha = request.GET.get('id')
    if id_cancha:
        cancha = get_object_or_404(Cancha, id=id_cancha)
        form = CanchaForm(instance=cancha)

    if request.method == 'POST':
        if cancha:
            form = CanchaForm(request.POST, instance=cancha)
        else:
            form = CanchaForm(request.POST)

    if form.is_valid():
        form.save()
        
    return render(request, 'form_canchas.html', {'form':form})

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

@api_view(['GET'])
def categoria_count(request):
    try:
        cantidad = Categoria.objects.count()
        return JsonResponse(
            {
                'cantidad':cantidad
            },
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({'message':str(e)},status=400)
    

# @api_view(['GET'])
# def productos_en_unidades(request):
#     try:
#         productos = Productos.objects.filter(unidades='u')
#         return JsonResponse(
#             ProductoSerializer(productos,many=True).data,
#             safe=False,
#             status=200,
#         )
#     except Exception as e:
#         return JsonResponse({'message':str(e)},status=400)


@api_view(['GET'])
def canchas_por_tipo(request):

    tipo = 'Concreto'
    
    try:
        canchas = Cancha.objects.filter(tipo_superficie=tipo)
        if not canchas.exists():
            return JsonResponse({'message': f'No se encontraron canchas del tipo "{tipo}".'}, status=404)
        
        return JsonResponse(
            CanchaSerializer(canchas, many=True).data,
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=400)
    

@api_view(['GET'])
def reporte_canchas(request):

    tipo = 'Concreto'
    
    try:
        canchas = Cancha.objects.filter(tipo_superficie=tipo)
        cantidad = canchas.count()
        
        return JsonResponse(
            ReporteCanchasSerializer({
                'cantidad':cantidad,
                'canchas':canchas
            }).data,
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=400)
    

@api_view(['POST'])
def enviar_mensaje(request):
    cs = ContactSerializer(data=request.data)
    if cs.is_valid():
        return JsonResponse({'message':'Mensaje enviado correctamente'},status=200)
    else:
        return JsonResponse({'mensaje':cs.errors},status=400)
