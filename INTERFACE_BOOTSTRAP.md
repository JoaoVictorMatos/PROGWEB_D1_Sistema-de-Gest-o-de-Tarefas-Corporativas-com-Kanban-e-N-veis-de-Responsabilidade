# Interface Responsiva com Bootstrap - Kanban Corporativo

## Resumo da Interface

Uma interface completa e responsiva para gerenciamento de tarefas corporativas com Kanban, desenvolvida com **Bootstrap 5.3**.

### ✨ Características Principais

#### 📊 Dashboard Kanban

- Visualização em 5 colunas (Backlog, A Fazer, Em Andamento, Em Revisão, Concluído)
- Estatísticas com cards coloridos
- Hover effects e animações suaves
- 100% responsivo para mobile, tablet e desktop

#### 📋 Gerenciamento de Tarefas

- **Criar**: Formulário com validação
- **Editar**: Alterar status, prioridade e responsável
- **Visualizar**: Detalhes completos da tarefa
- **Deletar**: Com confirmação de segurança
- **Listar**: Com filtros por status, prioridade e projeto

#### 📁 Gerenciamento de Projetos

- Lista de projetos com cards
- Detalhes do projeto
- Tarefas agrupadas por projeto
- Visualização em tabela responsiva

#### 🎨 Design

- **Navbar** com menu responsivo
- **Footer** com informações
- **Cards** com efeitos hover
- **Badges** coloridas por status/prioridade
- **Botão flutuante** para criar tarefa
- **Formulários** bem estruturados
- **Alertas** para feedback do usuário

#### 📱 Responsividade

- Mobile first design
- Breakpoints Bootstrap (xs, sm, md, lg, xl)
- Grid de 12 colunas flexível
- Navbar mobile collapse

### 🚀 Como Usar

#### 1. Rotas Disponíveis

| Rota                     | Descrição                    |
| ------------------------ | ---------------------------- |
| `/`                      | Dashboard Kanban             |
| `/tarefas/`              | Lista de tarefas             |
| `/tarefas/criar/`        | Criar nova tarefa            |
| `/tarefas/<id>/`         | Detalhes da tarefa           |
| `/tarefas/<id>/editar/`  | Editar tarefa                |
| `/tarefas/<id>/deletar/` | Deletar tarefa               |
| `/projetos/`             | Lista de projetos            |
| `/projetos/<id>/`        | Detalhes do projeto          |
| `/admin/`                | Painel administrativo Django |

#### 2. Requisitos

- Python 3.8+
- Django 4.0+
- PostgreSQL (conforme configurado)

#### 3. Instalação de Dependências

```bash
pip install -r requirements.txt
```

#### 4. Executar Migrações

```bash
python manage.py migrate
```

#### 5. Criar Superusuário (opcional)

```bash
python manage.py createsuperuser
```

#### 6. Iniciar Servidor

```bash
python manage.py runserver
```

Acesse: `http://localhost:8000`

### 📊 Cores por Status

| Status       | Cor               |
| ------------ | ----------------- |
| Backlog      | Cinza (#95a5a6)   |
| A Fazer      | Laranja (#f39c12) |
| Em Andamento | Azul (#3498db)    |
| Em Revisão   | Rosa (#e91e63)    |
| Concluído    | Verde (#27ae60)   |

### 🎯 Cores por Prioridade

- **Alta**: Vermelho (#e74c3c)
- **Média**: Laranja (#f39c12)
- **Baixa**: Verde (#27ae60)

### 🔧 Customização

#### Alterar Cores

Editar em `base.html` > `<style>`

#### Adicionar Ícones

Bootstrap Icons CDN já está incluído. Procure por `bi bi-*`

#### Modificar Layout

- Colunas Kanban: alterar em `dashboard.html`
- Cards: customizar CSS em `base.html`

### 📱 Compatibilidade

- ✅ Chrome, Firefox, Safari, Edge
- ✅ Desktop, Tablet, Mobile
- ✅ Bootstrap 5.3+
- ✅ Sem dependências JavaScript externas

### 📝 Estrutura de Arquivos

```
tarefas/
├── templates/tarefas/
│   ├── base.html              # Template base com navbar
│   ├── dashboard.html         # Quadro Kanban
│   ├── lista_tarefas.html    # Lista com filtros
│   ├── criar_tarefa.html     # Formulário criação
│   ├── editar_tarefa.html    # Formulário edição
│   ├── detalhe_tarefa.html   # Página de detalhes
│   ├── confirmar_deletar.html # Confirmação exclusão
│   ├── lista_projetos.html   # Lista de projetos
│   └── detalhe_projeto.html  # Detalhes projeto
├── views.py                   # Lógica das views
├── models.py                  # Modelos (já existentes)
├── admin.py                   # Admin Django customizado
└── urls.py                    # URLs da app
```

### 🎓 Exemplos de Uso

#### Acessar Dashboard

```
GET /
```

#### Criar Tarefa

```
POST /tarefas/criar/
{
    "titulo": "Minha tarefa",
    "descricao": "Descrição detalhada",
    "projeto": 1,
    "prioridade": "ALTA",
    "responsavel": 1,
    "data_entrega": "2024-12-31"
}
```

#### Filtrar Tarefas

```
GET /tarefas/?status=EM_ANDAMENTO&prioridade=ALTA&projeto=1
```

### 🐛 Troubleshooting

**Problema**: Página em branco

- Verifique se Django está rodando
- Verifique INSTALLED_APPS no settings.py

**Problema**: Templates não encontrados

- Verifique pasta `tarefas/templates/tarefas/`
- Verifique TEMPLATES em settings.py

**Problema**: Erro de banco de dados

- Execute: `python manage.py migrate`

### 📚 Documentação

- [Bootstrap 5 Docs](https://getbootstrap.com/docs/5.3/)
- [Bootstrap Icons](https://icons.getbootstrap.com/)
- [Django Docs](https://docs.djangoproject.com/)

---

**Desenvolvido com ❤️ usando Bootstrap 5.3**
