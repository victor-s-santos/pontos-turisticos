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
        return Response({'teste': 'Apenas um teste'})

    def create(self, request, *args, **kwargs):
        return Response({'Olá': request.data['nome']})

    def destroy(self, request, *args, **kwargs):
        pass