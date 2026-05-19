from django.contrib import admin
from .models import Departamento, PerfilUsuario, Projeto, Tarefa

@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')

@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ('user', 'departamento', 'cargo')
    list_filter = ('departamento',)

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_inicio', 'prazo')

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'projeto', 'responsavel', 'status', 'prioridade', 'data_entrega')
    list_filter = ('status', 'prioridade', 'projeto')
    search_fields = ('titulo', 'descricao')