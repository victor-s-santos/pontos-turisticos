from rest_framework.serializers import ModelSerializer
from endereco.models import Endereco


class EnderecoSerializer(ModelSerializer):
	class Meta:
		model = Endereco
		fields = ('pais', 'estado', 'cidade', 'linha1')