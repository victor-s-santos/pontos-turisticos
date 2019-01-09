from rest_framework.viewsets import ModelViewSet
from avaliacoes.models import Avaliacoes
from .serializers import AvaliacoesSerializer

class AvaliacoesViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Avaliacoes.objects.all()
    serializer_class = AvaliacoesSerializer
