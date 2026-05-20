from django.contrib import admin
from .models import Departamento, PerfilUsuario, Projeto, Tarefa

admin.site.site_header = "Kanban Corporativo - Administração"
admin.site.site_title = "Kanban Corp"
admin.site.index_title = "Painel de Gestão"

@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    search_fields = ('nome',)

@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ('user', 'cargo', 'nivel_responsabilidade', 'departamento')
    list_filter = ('nivel_responsabilidade', 'departamento')
    search_fields = ('user__username', 'cargo')

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_inicio', 'prazo')
    search_fields = ('nome',)

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'projeto', 'responsavel', 'status', 'prioridade', 'data_entrega')
    list_filter = ('status', 'prioridade', 'projeto')
    search_fields = ('titulo', 'descricao')