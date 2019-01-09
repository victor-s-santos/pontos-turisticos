from django.db import models

class Atracoes(models.Model):
	nome = models.CharField(max_length=200)
	descricao = models.TextField()
	horario = models.TextField()
	idade_min = models.IntegerField()
	class Meta:
		verbose_name_plural = 'Atrações'

	def __str__(self):
		return self.nome

# Create your models here.
