from django.contrib import admin
from .models import PontosTuristicos
from .actions import aprova_comentarios, reprova_comentarios

class PontosTuristicosAdmin(admin.ModelAdmin):
	list_display = ['nome', 'aprovado']
	actions = [aprova_comentarios, reprova_comentarios]

admin.site.register(PontosTuristicos, PontosTuristicosAdmin)
# Register your models here.
