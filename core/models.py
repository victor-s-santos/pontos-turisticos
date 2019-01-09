from django.db import models
from atracoes.models import Atracoes
from comentarios.models import Comentarios
from avaliacoes.models import Avaliacoes
from endereco.models import Endereco


class PontosTuristicos(models.Model):
	nome = models.CharField(max_length=200)
	descricao = models.TextField()
	aprovado = models.BooleanField(default=False)
	atracoes = models.ManyToManyField(Atracoes)
	comentarios = models.ManyToManyField(Comentarios)
	avaliacoes = models.ManyToManyField(Avaliacoes)
	endereco = models.ForeignKey(
		Endereco, on_delete=models.CASCADE, null=True, blank=True )

	class Meta:
		verbose_name_plural = 'pontos turisticos'

	def __str__(self):
		return self.nome
# Create your models here.
