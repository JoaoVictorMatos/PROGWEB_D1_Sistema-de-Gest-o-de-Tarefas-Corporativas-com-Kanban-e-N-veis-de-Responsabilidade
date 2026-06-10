from django.contrib import admin
from django.utils.html import format_html
from .models import Departamento, PerfilUsuario, Projeto, Tarefa

admin.site.site_header = "Painel Administrativo"
admin.site.site_title = "Kanban Corp"
admin.site.index_title = "Administração do Site"


def badge(texto, cor):
    return format_html(
        '<span class="badge rounded-pill" '
        'style="background-color:{};color:#fff;font-size:.8rem;padding:.4em .7em;">{}</span>',
        cor, texto,
    )


@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao_curta')
    search_fields = ('nome', 'descricao')
    list_per_page = 25

    fieldsets = (
        ('Informações do Departamento', {'fields': ('nome',)}),
        ('Descrição', {'fields': ('descricao',), 'classes': ('collapse',)}),
    )

    @admin.display(description='Descrição')
    def descricao_curta(self, obj):
        if obj.descricao and len(obj.descricao) > 50:
            return obj.descricao[:50] + '...'
        return obj.descricao or '-'


@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ('user', 'cargo', 'nivel_responsabilidade_badge', 'departamento')
    list_filter = ('nivel_responsabilidade', 'departamento')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'cargo')
    list_per_page = 25
    list_select_related = ('user', 'departamento')

    fieldsets = (
        ('Usuário', {'fields': ('user',)}),
        ('Informações Profissionais', {'fields': ('cargo', 'departamento')}),
        ('Responsabilidade', {'fields': ('nivel_responsabilidade',)}),
    )

    @admin.display(description='Nível')
    def nivel_responsabilidade_badge(self, obj):
        colors = {
            'COLABORADOR': '#0d6efd',
            'LIDER': '#fd7e14',
            'GERENTE': '#dc3545',
            'DIRETOR': '#6f42c1',
        }
        cor = colors.get(obj.nivel_responsabilidade, '#6c757d')
        return badge(obj.get_nivel_responsabilidade_display(), cor)


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_inicio', 'prazo', 'total_tarefas')
    search_fields = ('nome', 'descricao')
    list_per_page = 25
    date_hierarchy = 'data_inicio'
    readonly_fields = ('data_inicio',)
    list_select_related = True

    fieldsets = (
        ('Informações Básicas', {'fields': ('nome',)}),
        ('Datas', {'fields': ('data_inicio', 'prazo'), 'classes': ('collapse',)}),
        ('Descrição', {'fields': ('descricao',)}),
    )

    @admin.display(description='Tarefas')
    def total_tarefas(self, obj):
        return badge(str(obj.tarefas.count()), '#0d6efd')


@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'projeto', 'responsavel_nome', 'status_badge', 'prioridade_badge', 'data_entrega')
    list_filter = ('status', 'prioridade', 'projeto', 'data_criacao')
    search_fields = ('titulo', 'descricao', 'projeto__nome')
    list_per_page = 25
    date_hierarchy = 'data_criacao'
    readonly_fields = ('data_criacao',)
    list_select_related = ('projeto', 'responsavel')

    fieldsets = (
        ('Informações Básicas', {'fields': ('titulo', 'projeto')}),
        ('Descrição', {'fields': ('descricao',)}),
        ('Atribuição', {'fields': ('responsavel',)}),
        ('Status e Prioridade', {'fields': ('status', 'prioridade')}),
        ('Datas', {'fields': ('data_criacao', 'data_entrega'), 'classes': ('collapse',)}),
    )

    actions = ['marcar_concluido', 'marcar_andamento']

    @admin.display(description='Responsável')
    def responsavel_nome(self, obj):
        if obj.responsavel:
            return obj.responsavel.get_full_name() or obj.responsavel.username
        return '-'

    @admin.display(description='Status')
    def status_badge(self, obj):
        colors = {
            'BACKLOG': '#6c757d',
            'A_FAZER': '#fd7e14',
            'EM_ANDAMENTO': '#0d6efd',
            'REVISAO': '#d63384',
            'CONCLUIDO': '#198754',
        }
        cor = colors.get(obj.status, '#6c757d')
        return badge(obj.get_status_display(), cor)

    @admin.display(description='Prioridade')
    def prioridade_badge(self, obj):
        colors = {
            'BAIXA': '#198754',
            'MEDIA': '#fd7e14',
            'ALTA': '#dc3545',
        }
        cor = colors.get(obj.prioridade, '#6c757d')
        return badge(obj.get_prioridade_display(), cor)

    @admin.action(description='Marcar como Concluído')
    def marcar_concluido(self, request, queryset):
        updated = queryset.update(status='CONCLUIDO')
        self.message_user(request, f'{updated} tarefa(s) marcada(s) como concluída(s).')

    @admin.action(description='Marcar como Em Andamento')
    def marcar_andamento(self, request, queryset):
        updated = queryset.update(status='EM_ANDAMENTO')
        self.message_user(request, f'{updated} tarefa(s) marcada(s) como em andamento.')
