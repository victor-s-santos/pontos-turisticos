from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from core.api.viewsets import PontosTuristicosViewSet
from atracoes.api.viewsets import AtracoesViewSet
from endereco.api.viewsets import EnderecoViewSet
from comentarios.api.viewsets import ComentariosViewSet
from avaliacoes.api.viewsets import AvaliacoesViewSet


router = routers.DefaultRouter()
router.register(r'pontosturisticos', PontosTuristicosViewSet, base_name = 'PontosTuristicos')
router.register(r'atracoes', AtracoesViewSet)
router.register(r'endereco', EnderecoViewSet)
router.register(r'comentarios', ComentariosViewSet)
router.register(r'avaliacoes', AvaliacoesViewSet)

urlpatterns = [
	path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#I need to do the line above because this project still in development mode