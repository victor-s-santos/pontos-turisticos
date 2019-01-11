from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.models import PontosTuristicos
from .serializers import PontosTuristicosSerializer
from rest_framework.decorators import action

class PontosTuristicosViewSet(ModelViewSet):
    """
    The simplest viewset for viewiing and editing accounts, but
    overwriting the get_queryset.
    """
    serializer_class = PontosTuristicosSerializer

    def get_queryset(self):
    	return PontosTuristicos.objects.filter(aprovado = True)

    def list(self, request, *args, **kwargs):
                return super(PontosTuristicosViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(PontosTuristicosViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
                return super(PontosTuristicosViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
                return super(PontosTuristicosViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
                return super(PontosTuristicosViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
                return super(PontosTuristicosViewSet, self).partial_update(request, *args, **kwargs)

    @action(methods=['get', 'post'], detail=True)
    def denunciar(self, request, pk=None):
        pass

    @action(methods=['get'], detail=False)
    def geral_action(self, request):
        pass