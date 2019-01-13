from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from core.models import PontosTuristicos
from .serializers import PontosTuristicosSerializer
from rest_framework.decorators import action

class PontosTuristicosViewSet(ModelViewSet):
    """
    The simplest viewset for viewiing and editing accounts, but
    overwriting the get_queryset.
    """
    serializer_class = PontosTuristicosSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('nome', 'descricao', 'endereco__cidade')
    lookup_field = ('id')#I prefer to keep the default value


    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontosTuristicos.objects.all()

        if id:
            queryset = PontosTuristicos.objects.filter(pk=id)

        if nome:
            queryset = queryset.filter(nome__iexact=nome)

        if descricao:
            queryset = queryset.filter(descricao__iexact=descricao)

        return queryset

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