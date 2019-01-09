from rest_framework.viewsets import ModelViewSet
from core.models import PontosTuristicos
from .serializers import PontosTuristicosSerializer

class PontosTuristicosViewSet(ModelViewSet):
    """
    queryset = PontosTuristicos.objects.filter(aprovado = True)
    A ideia mais facil era usar o filter no queryset sem grandes alterações
    no entanto, por motivos de aprendizagem eu farei da melhor forma neste app
    """
    serializer_class = PontosTuristicosSerializer

    def get_queryset(self):
    	return PontosTuristicos.objects.filter(aprovado = True)

