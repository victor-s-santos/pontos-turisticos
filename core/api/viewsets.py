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

    #def list(self, request, *args, **kwargs):
    	"""
    	By default the drf returns a list of objects wich are returned by the get_queryset.
    	"""
    #	return Response({'only_a_test': 'it works!'})

"""    def create(self, request, *args, **kwargs):
        
        #By this way the drf always returns(post) the follow 
        #dictionary.  
        
        return Response({'Hello': request.data['nome']})


    def destroy(self, request, *args, **kwargs):
        pass

    def retrieve(self, request, *args, **kwargs):
        pass

    def update(self, request, *args, **kwargs):
        pass

    def partial_update(self, request, *args, **kwargs):
        pass
""
    @action(methods=['get'], detail=True)
    def denunciar(self, request, pk=None):
        pass"""