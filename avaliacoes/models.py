from django.contrib.auth.models import User
from django.db import models

class Avaliacoes(models.Model):
	usuario = models.ForeignKey(User, on_delete=models.CASCADE)
	comentario = models.TextField(null=True, blank=True)
	nota = models.DecimalField(max_digits=3, decimal_places=2)
	data = models.DateField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'avaliacoes'

	def __str__(self):
		return self.usuario.username

# Create your models here.
