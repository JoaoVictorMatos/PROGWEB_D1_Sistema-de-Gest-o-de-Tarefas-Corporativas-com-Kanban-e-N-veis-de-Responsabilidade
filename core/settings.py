import os

# Altere a lista de INSTALLED_APPS para incluir o seu app
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tarefas', # Seu app cadastrado
]

# Configuração do PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'kanban_db'),
        'USER': os.environ.get('DB_USER', 'postgres_admin'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'senha_secreta_gac116'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': '5432',
    }
}