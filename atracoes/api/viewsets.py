from rest_framework.viewsets import ModelViewSet
from atracoes.models import Atracoes
from .serializers import AtracoesSerializer

class AtracoesViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Atracoes.objects.all()
    serializer_class = AtracoesSerializer


