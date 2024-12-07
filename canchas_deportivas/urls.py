from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'categorias',views.CategoriaViewSet)

urlpatterns = [
    path('contact/<str:name>',views.contact ,name='contacto'),
    # path('categorias/',views.categorias , name='categoria'),
    # path('canchas/',views.canchaFormView, name='cancha'),
    # path('', views.index,name='index'),
    # path('',include(router.urls)),
    path('categoria/',views.CategoriaCreateView.as_view()),
    path('categoria/cantidad/',views.categoria_count),
    path('canchas/filtar/tipo/',views.canchas_por_tipo),
    path('canchas/reporte/',views.reporte_canchas),
    path('contact/',views.enviar_mensaje,name='contact'),
]