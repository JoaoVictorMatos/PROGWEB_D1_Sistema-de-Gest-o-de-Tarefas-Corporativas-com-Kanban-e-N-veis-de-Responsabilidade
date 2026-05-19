# Sistema de Gestão de Tarefas Corporativas (Kanban)

## 📖 1. Sobre o Projeto
Este projeto consiste em um Sistema de Gestão de Tarefas Corporativas baseado na metodologia ágil Kanban, desenvolvido como o **Trabalho Prático 1** para a disciplina **GAC116 - Programação Web (2026/1)**. 

A aplicação foi modelada e implementada utilizando o framework **Django**, com persistência em um banco de dados relacional **PostgreSQL**, interface responsiva construída com **Bootstrap**, e containerização completa via **Docker**.

A entrega e a defesa deste projeto são de extrema importância, valendo um total de **45,0 pontos** na nota semestral e computando **seis presenças (12 créditos)** nas aulas teóricas de sábado.

---

## 👥 2. Contribuidores (Grupo)
Conforme as diretrizes obrigatórias estabelecidas no edital do trabalho, a equipe é composta por estudantes da disciplina, onde todos os integrantes constam como contribuidores ativos no projeto do GitHub e realizaram pelo menos um commit no ecossistema da aplicação:

* **João Victor Matos** - [GitHub Profile](https://github.com/JoaoVictorMatos)
* **Lucas de Oliveira Pereira** - [GitHub Profile](https://github.com/lucaspereirap7)
* **[Nome do Integrante 3]** - [GitHub Profile](https://github.com/) (Se aplicável)

---

## 📋 3. Análise de Requisitos

O escopo do sistema foi projetado para simular um ambiente corporativo de alta produtividade, mapeando as necessidades de fluxo de trabalho de uma empresa através de requisitos claros.

### Requisitos Funcionais (RF)
* **RF001 - Autenticação de Usuários:** O sistema deve possuir controle de acesso seguro por meio de login e senha para separar as camadas de visualização.
* **RF002 - Ambiente Administrativo Isolado:** O sistema deve fornecer um ambiente administrativo protegido para que gerentes e diretores gerenciem cadastros macro.
* **RF003 - Painel Kanban (Ambiente do Usuário):** O colaborador autenticado deve ter acesso a um ambiente exclusivo para visualizar e interagir com suas tarefas corporativas.
* **RF004 - Mapeamento Relacional de Tarefas:** Cada tarefa cadastrada deve possuir, obrigatoriamente, vínculos com tabelas relacionais do banco de dados (Projeto, Responsável e Coluna de Status).
* **RF005 - Atribuição de Responsabilidades:** O sistema deve permitir designar um colaborador específico como o responsável técnico por cada atividade dentro do projeto.
* **RF006 - Movimentação de Status:** O usuário deve ser capaz de alterar o status de suas tarefas, progredindo-as entre as colunas do Kanban (*Backlog, A Fazer, Em Andamento, Revisão, Concluído*).

### Requisitos Não Funcionais (RNF)
* **RNF001 - Persistência Relacional Robustecida:** Uso obrigatório de um banco de dados relacional (PostgreSQL) focado na integridade referencial dos dados corporativos.
* **RNF002 - Interface Amigável e Responsiva:** A interface do usuário deve se adaptar de forma fluida a telas de smartphones, tablets e desktops utilizando o framework Bootstra.
* **RNF003 - Portabilidade e Isolamento de Ambiente:** Utilização de conteinerização com Docker para garantir que o projeto rode com as mesmas dependências em qualquer sistema operacional.
* **RNF004 - Versionamento Colaborativo:** Controle de versão e histórico de alterações gerenciados estritamente via Git e hospedado em repositório público no GitHub.

---

## 🔒 4. Segurança e Níveis de Acesso

A segurança da aplicação foi estruturada seguindo as boas práticas de desenvolvimento web e os requisitos do edital, dividindo o ecossistema em duas camadas de proteção:

1. **Criptografia de Credenciais (Django Auth):** Nenhuma senha é armazenada em texto plano no banco de dados. O sistema utiliza algoritmos de hash robustos nativos do Django (PBKDF2 com SHA256), impedindo a leitura das credenciais mesmo em caso de vazamento do banco de dados.
2. **Ambiente Administrativo Protegido (`/admin`):** Acessível utilizando a estrutura do `djangoAdmin`. Este painel é restrito a colaboradores que possuam privilégios de administrador (`is_staff` ou `is_superuser`), permitindo a gerência de novos usuários, criação de departamentos e auditoria geral do sistema.
3. **Ambiente do Usuário Autenticado:** Protegido por autenticação obrigatória. Um colaborador comum só consegue visualizar as tarefas e interagir com o quadro Kanban após validar sua identidade na tela de login. Tentativas de acesso direto às URLs internas por usuários anônimos são barradas e redirecionadas.

---

## 🛠️ 5. Tecnologias Utilizadas
* **Backend:** Django Framework (Python)
* **Frontend:** HTML5, CSS3, JavaScript e Bootstrap
* **Banco de Dados:** PostgreSQL (SGBD Relacional) 
* **Ambiente e Deploy:** Docker, Docker Compose e GitHub

---

## 🚀 6. Como Executar o Projeto Localmente (Docker)

A infraestrutura do projeto foi totalmente preparada utilizando Docker para que você não precise instalar o Python ou o PostgreSQL localmente na sua máquina física.

### Pré-requisitos
* Possuir o **Docker** e o **Docker Compose** instalados na máquina de desenvolvimento.

### Passo a passo para executar
1. Suba os serviços do banco e da aplicação:

```bash
docker compose up --build
```

2. Em outro terminal, aplique as migrações no banco:

```bash
docker compose run --rm web python manage.py migrate
```

3. Crie um usuário administrador para acessar o painel `/admin`:

```bash
docker compose run --rm web python manage.py createsuperuser
```

4. Abra a aplicação em:

```text
http://localhost:8000/admin/
```

### Situação atual para o checkpoint1
* A modelagem do banco já está definida em `tarefas/models.py`.
* O admin já está registrado em `tarefas/admin.py`.
* O projeto já possui `manage.py`, `core/urls.py` e `core/wsgi.py`, então pode ser executado via Django.

---

### Como rodar (modo rápido)

1. Subir containers:

```bash
docker compose up --build -d
```

2. Aplicar migrações:

```bash
docker compose run --rm web python manage.py migrate
```

3. Criar superusuário:

```bash
docker compose run --rm web python manage.py createsuperuser
```

Se precisar de uma conta de demonstração rápida (apenas para apresentação local):

```powershell
$env:DJANGO_SUPERUSER_PASSWORD='Admin1234'; docker compose run --rm web python manage.py createsuperuser --noinput --username admin --email admin@example.com
```

Abra o admin em:

```text
http://localhost:8000/admin/
```

---

### Arquivo `.env` (opcional)

Você pode usar um `.env` com essas variáveis ao rodar os comandos acima no mesmo terminal:

```
DB_NAME=kanban_db
DB_USER=postgres_admin
DB_PASSWORD=senha_secreta_gac116
DB_HOST=db
DB_PORT=5432
DEBUG=1
SECRET_KEY=django-insecure-dev-key-change-me
ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0
```

Troque `SECRET_KEY` e `DB_PASSWORD` antes de publicar o projeto.

---

### Popular dados de demonstração (opcional)

Para inserir alguns registros básicos use o shell do Django:

```bash
docker compose run --rm web python manage.py shell

# cole no shell:
from tarefas.models import Departamento, Projeto, Tarefa
from django.contrib.auth import get_user_model
User = get_user_model()
dept = Departamento.objects.create(nome='TI', descricao='Tecnologia')
proj = Projeto.objects.create(nome='Projeto Demo', descricao='Projeto para checkpoint1', prazo='2026-12-31')
user = User.objects.filter(is_superuser=False).first()
Tarefa.objects.create(titulo='Tarefa exemplo', descricao='Descrição', projeto=proj, responsavel=user, status='BACKLOG', prioridade='MEDIA')
exit()
```

---

### Parar e remover

```bash
docker compose down
# para remover volumes (apaga dados do banco):
docker compose down -v
```

---

### Executar sem Docker (opcional)

```bash
python -m venv .venv
source .venv/bin/activate   # ou .venv\Scripts\Activate.ps1 no Windows
pip install -r requirements.txt
export DB_NAME=kanban_db DB_USER=postgres_admin DB_PASSWORD=senha_secreta_gac116 DB_HOST=localhost
python manage.py migrate
python manage.py runserver
```

---


   