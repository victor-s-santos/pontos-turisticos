from django.contrib.auth.models import User
from django.db import models

class Comentarios(models.Model):
	usuario = models.ForeignKey(User, on_delete=models.CASCADE)
	comentario = models.TextField()
	data = models.DateField(auto_now_add=True)
	aprovado = models.BooleanField(default=True)

	class Meta:
		verbose_name_plural = 'comentarios'


	def __str__(self):
		return self.usuario.username
# Create your models here.
