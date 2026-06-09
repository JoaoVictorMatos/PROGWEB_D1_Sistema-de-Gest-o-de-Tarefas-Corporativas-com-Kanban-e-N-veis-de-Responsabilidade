from django.contrib import admin
from .models import Departamento, PerfilUsuario, Projeto, Tarefa

# Customização do header do admin
admin.site.site_header = "📊 Kanban Corporativo - Administração"
admin.site.site_title = "Kanban Corp"
admin.site.index_title = "Painel de Gestão do Kanban"


@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao_curta')
    search_fields = ('nome', 'descricao')
    list_per_page = 25
    
    fieldsets = (
        ('Informações do Departamento', {
            'fields': ('nome',)
        }),
        ('Descrição', {
            'fields': ('descricao',),
            'classes': ('collapse',)
        }),
    )
    
    def descricao_curta(self, obj):
        return obj.descricao[:50] + '...' if obj.descricao and len(obj.descricao) > 50 else obj.descricao or '-'
    descricao_curta.short_description = 'Descrição'


@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ('user', 'cargo', 'nivel_responsabilidade_badge', 'departamento')
    list_filter = ('nivel_responsabilidade', 'departamento')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'cargo')
    list_per_page = 25
    
    fieldsets = (
        ('Usuário', {
            'fields': ('user',)
        }),
        ('Informações Profissionais', {
            'fields': ('cargo', 'departamento')
        }),
        ('Responsabilidade', {
            'fields': ('nivel_responsabilidade',),
        }),
    )
    
    def nivel_responsabilidade_badge(self, obj):
        colors = {
            'COLABORADOR': '#3498db',
            'LIDER': '#f39c12',
            'GERENTE': '#e74c3c',
            'DIRETOR': '#9b59b6',
        }
        color = colors.get(obj.nivel_responsabilidade, '#95a5a6')
        return f'<span style="background-color: {color}; color: white; padding: 4px 8px; border-radius: 3px; font-weight: bold;">{obj.get_nivel_responsabilidade_display()}</span>'
    nivel_responsabilidade_badge.short_description = 'Nível'
    nivel_responsabilidade_badge.allow_tags = True


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_inicio', 'prazo', 'total_tarefas')
    search_fields = ('nome', 'descricao')
    list_per_page = 25
    date_hierarchy = 'data_inicio'
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('nome',)
        }),
        ('Datas', {
            'fields': ('data_inicio', 'prazo'),
            'classes': ('collapse',)
        }),
        ('Descrição', {
            'fields': ('descricao',),
        }),
    )
    
    readonly_fields = ('data_inicio',)
    
    def total_tarefas(self, obj):
        count = obj.tarefas.count()
        return f'<span style="background-color: #4a90e2; color: white; padding: 3px 8px; border-radius: 3px; font-weight: bold;">{count}</span>'
    total_tarefas.short_description = 'Tarefas'
    total_tarefas.allow_tags = True


@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'projeto', 'responsavel_nome', 'status_badge', 'prioridade_badge', 'data_entrega')
    list_filter = ('status', 'prioridade', 'projeto', 'data_criacao')
    search_fields = ('titulo', 'descricao', 'projeto__nome')
    list_per_page = 25
    date_hierarchy = 'data_criacao'
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('titulo', 'projeto')
        }),
        ('Descrição', {
            'fields': ('descricao',),
        }),
        ('Atribuição', {
            'fields': ('responsavel',),
        }),
        ('Status e Prioridade', {
            'fields': ('status', 'prioridade'),
        }),
        ('Datas', {
            'fields': ('data_criacao', 'data_entrega'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ('data_criacao',)
    
    filter_horizontal = ()
    
    def responsavel_nome(self, obj):
        if obj.responsavel:
            return obj.responsavel.get_full_name() or obj.responsavel.username
        return '-'
    responsavel_nome.short_description = 'Responsável'
    
    def status_badge(self, obj):
        colors = {
            'BACKLOG': '#95a5a6',
            'A_FAZER': '#f39c12',
            'EM_ANDAMENTO': '#3498db',
            'REVISAO': '#e91e63',
            'CONCLUIDO': '#27ae60',
        }
        color = colors.get(obj.status, '#95a5a6')
        return f'<span style="background-color: {color}; color: white; padding: 4px 8px; border-radius: 3px; font-weight: bold;">{obj.get_status_display()}</span>'
    status_badge.short_description = 'Status'
    status_badge.allow_tags = True
    
    def prioridade_badge(self, obj):
        colors = {
            'BAIXA': '#27ae60',
            'MEDIA': '#f39c12',
            'ALTA': '#e74c3c',
        }
        color = colors.get(obj.prioridade, '#95a5a6')
        return f'<span style="background-color: {color}; color: white; padding: 4px 8px; border-radius: 3px; font-weight: bold;">🚩 {obj.get_prioridade_display()}</span>'
    prioridade_badge.short_description = 'Prioridade'
    prioridade_badge.allow_tags = True
    
    actions = ['marcar_concluido', 'marcar_andamento']
    
    def marcar_concluido(self, request, queryset):
        updated = queryset.update(status='CONCLUIDO')
        self.message_user(request, f'{updated} tarefa(s) marcada(s) como concluída(s).')
    marcar_concluido.short_description = '✓ Marcar como Concluído'
    
    def marcar_andamento(self, request, queryset):
        updated = queryset.update(status='EM_ANDAMENTO')
        self.message_user(request, f'{updated} tarefa(s) marcada(s) como em andamento.')
    marcar_andamento.short_description = '▶ Marcar como Em Andamento'