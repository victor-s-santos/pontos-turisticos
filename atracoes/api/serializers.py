from rest_framework.serializers import ModelSerializer
from atracoes.models import Atracoes


class AtracoesSerializer(ModelSerializer):
	class Meta:
		model = Atracoes
		fields = ('nome', 'descricao', 'horario', 'idade_min', 'foto')