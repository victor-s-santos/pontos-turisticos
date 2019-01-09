from django.db import models


class Endereco(models.Model):
	linha1 = models.CharField(max_length=200)
	linha2 = models.CharField(max_length=200, blank=True, null=True)
	cidade = models.CharField(max_length=100)
	estado = models.CharField(max_length=2)
	pais = models.CharField(max_length=100)
	longitude = models.IntegerField(blank=True, null=True)
	latitude = models.IntegerField(blank=True, null=True)

	class Meta:
		verbose_name_plural = 'Endereços'

	def __str__(self):
		return self.linha1
# Create your models here.
