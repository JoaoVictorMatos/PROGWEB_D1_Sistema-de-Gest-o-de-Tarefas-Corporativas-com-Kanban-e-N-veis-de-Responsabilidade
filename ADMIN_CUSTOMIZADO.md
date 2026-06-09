# Admin Django Customizado - Kanban Corporativo

## Visão Geral

O painel administrativo do Django foi totalmente customizado com:

- **CSS moderno** com gradientes, animações e responsividade
- **Badges coloridas** para status e prioridades
- **Fieldsets organizados** para melhor UX
- **Ações em lote** para gerenciamento rápido
- **Design responsivo** mobile-first

---

## 📁 Arquivos Criados

### 1. `tarefas/static/admin/css/custom_admin.css`

Arquivo CSS com todas as customizações visuais do admin:

- Cores temáticas com gradientes
- Hover effects em tabelas
- Botões melhorados
- Filtros e busca customizados
- Responsividade para mobile

### 2. `tarefas/templates/admin/base_site.html`

Template customizado que estende o base do admin:

- Header com branding do projeto
- Carregamento do CSS customizado
- Meta tags responsivas

### 3. `tarefas/admin.py` (Atualizado)

Configurações avançadas para cada modelo:

- Fieldsets organizados
- Badges com cores
- Ações em lote
- Readonly fields
- Hierarquia de datas
- Métodos customizados para exibição

---

## 🎨 Customizações por Modelo

### 📁 Departamento

- Lista de departamentos com nome e descrição
- Busca por nome e descrição
- 25 itens por página

**Fields customizados:**

```
- Informações do Departamento
  - nome
- Descrição (colapsável)
  - descricao
```

### 👤 Perfil de Usuário

- Exibe usuário, cargo, nível e departamento
- Filtros por nível e departamento
- Badge colorida para nível de responsabilidade

**Cores por Nível:**
| Nível | Cor |
|-------|-----|
| Colaborador | Azul (#3498db) |
| Líder | Laranja (#f39c12) |
| Gerente | Vermelho (#e74c3c) |
| Diretor | Roxo (#9b59b6) |

### 📊 Projeto

- Nome, data de início e prazo
- Total de tarefas do projeto (badge)
- Hierarquia de datas para filtro
- Campo data_inicio como readonly

**Fields customizados:**

```
- Informações Básicas
  - nome
- Datas (colapsável)
  - data_inicio (readonly)
  - prazo
- Descrição
  - descricao
```

### ✅ Tarefa

- Título, projeto, responsável, status e prioridade
- Badges coloridas para status e prioridade
- Ações em lote (Marcar como Concluído, Marcar como Em Andamento)
- Hierarquia de datas
- Campo data_criacao como readonly

**Cores por Status:**
| Status | Cor |
|--------|-----|
| Backlog | Cinza (#95a5a6) |
| A Fazer | Laranja (#f39c12) |
| Em Andamento | Azul (#3498db) |
| Em Revisão | Rosa (#e91e63) |
| Concluído | Verde (#27ae60) |

**Cores por Prioridade:**
| Prioridade | Cor |
|-----------|-----|
| Baixa | Verde (#27ae60) |
| Média | Laranja (#f39c12) |
| Alta | Vermelho (#e74c3c) |

**Ações em Lote:**

- ✓ Marcar como Concluído
- ▶ Marcar como Em Andamento

---

## 🔧 Configuração

### 1. Garantir que o Django está configurado corretamente

Em `core/settings.py`:

```python
# Certifique-se de que INSTALLED_APPS inclui:
INSTALLED_APPS = [
    'django.contrib.admin',  # ✓
    'django.contrib.auth',   # ✓
    'django.contrib.contenttypes',  # ✓
    'django.contrib.sessions',      # ✓
    'django.contrib.messages',      # ✓
    'django.contrib.staticfiles',   # ✓
    'tarefas.apps.TarefasConfig',
]

# TEMPLATES deve ter APP_DIRS = True
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,  # ✓ IMPORTANTE
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

### 2. Coletar arquivos estáticos

```bash
python manage.py collectstatic
```

### 3. Criar superusuário

```bash
python manage.py createsuperuser
```

### 4. Iniciar o servidor

```bash
python manage.py runserver
```

### 5. Acessar o admin

```
http://localhost:8000/admin/
```

---

## 🎯 Recursos da Interface

### ✨ Visual Enhancements

- **Gradientes**: Headers e botões com gradientes lineares
- **Sombras**: Efeitos de profundidade em cards e buttons
- **Transições**: Animações suaves em hover
- **Badges**: Indicadores coloridos inline
- **Responsividade**: Adapta-se a qualquer tamanho de tela

### 🔍 Filtragem Avançada

- Filtros por múltiplos critérios
- Busca em vários campos
- Hierarquia de datas para range filtering
- Filtros sidebar customizados

### 📋 Listagem Melhorada

- Tabelas com hover effects
- Paginação customizada
- 25 itens por página (configurável)
- Colunas customizadas

### 🎬 Ações em Lote

- Marcar tarefas como concluídas
- Marcar tarefas como em andamento
- Com feedback ao usuário

### 📱 Responsividade

- Mobile-friendly layout
- Botões full-width em telas pequenas
- Menus colapsáveis
- Texto reduzido em dispositivos pequenos

---

## 💡 Exemplos de Uso

### Atualizar múltiplas tarefas rapidamente

1. Acesse `/admin/tarefas/tarefa/`
2. Selecione as tarefas desejadas (checkboxes)
3. Escolha a ação no dropdown ("Marcar como Concluído")
4. Clique "Ir"

### Filtrar tarefas por status

1. No painel de tarefas, clique no status desejado na sidebar
2. A lista filtra automaticamente

### Buscar tarefas

1. Use a barra de busca para procurar por:
   - Título
   - Descrição
   - Nome do projeto

### Organizar fieldsets

- Clique em "(collapse)" para expandir/colapsar seções
- Facilita o gerenciamento de formulários longos

---

## 📊 Variáveis CSS Customizáveis

Em `custom_admin.css`, na seção `:root`:

```css
:root {
  --primary-color: #4a90e2; /* Azul principal */
  --secondary-color: #34495e; /* Cinza escuro */
  --success-color: #27ae60; /* Verde */
  --warning-color: #f39c12; /* Laranja */
  --danger-color: #e74c3c; /* Vermelho */
  --info-color: #3498db; /* Azul info */
  --light-color: #ecf0f1; /* Cinza claro */
  --dark-color: #2c3e50; /* Preto */
  --border-radius: 6px; /* Raio da borda */
}
```

Altere conforme necessário para customizar as cores globalmente.

---

## 🐛 Troubleshooting

### Problema: CSS não está sendo aplicado

**Solução:**

```bash
python manage.py collectstatic --clear
python manage.py runserver
```

### Problema: Templates não encontrados

**Solução:**
Verifique se a pasta `tarefas/templates/admin/` existe e contém `base_site.html`

### Problema: Badges não aparecem

**Solução:**
Em Django 3.2+, use `format_html()` ao invés de `.allow_tags = True`:

```python
from django.utils.html import format_html

def status_badge(self, obj):
    color = '#27ae60'
    return format_html(
        '<span style="background-color: {}; color: white; padding: 4px 8px; border-radius: 3px;">{}</span>',
        color,
        obj.get_status_display()
    )
```

---

## 🚀 Próximos Passos

### Implementar

- [ ] Inline editing na listagem
- [ ] Exportar dados para CSV
- [ ] Relatórios customizados
- [ ] Gráficos de dashboard
- [ ] Integração com Dark Mode

### Adicionar

- [ ] Ícones mais visuais
- [ ] Animações ao abrir/fechar
- [ ] Botões de ação rápida
- [ ] Confirmação modal para ações perigosas

---

## 📚 Referências

- [Django Admin Documentation](https://docs.djangoproject.com/en/stable/ref/contrib/admin/)
- [Django Admin Customization](https://docs.djangoproject.com/en/stable/ref/contrib/admin/css-customizing/)
- [Bootstrap Colors](https://getbootstrap.com/docs/5.0/customize/color/)

---

**Admin Customizado com ❤️ para Django**
