from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.models import PontosTuristicos
from .serializers import PontosTuristicosSerializer

class PontosTuristicosViewSet(ModelViewSet):
    """
    The simplest viewset for viewiing and editing accounts, but
    overwriting the get_queryset.
    """
    serializer_class = PontosTuristicosSerializer

    def get_queryset(self):
    	return PontosTuristicos.objects.filter(aprovado = True)

    def list(self, request, *args, **kwargs):
    	"""
    	By default the drf returns a list of objects wich are returned by the get_queryset.
    	"""
    	return Response({'only_a_test': 'it works!'})

