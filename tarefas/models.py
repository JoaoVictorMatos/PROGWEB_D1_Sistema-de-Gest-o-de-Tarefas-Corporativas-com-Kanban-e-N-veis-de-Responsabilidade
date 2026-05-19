from django.db import models
from django.contrib.auth.models import User

class Departamento(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Departamento")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")

    def __str__(self):
        return self.nome

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True, blank=True)
    cargo = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username} - {self.cargo}"

class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data_inicio = models.DateField(auto_now_add=True)
    prazo = models.DateField()

    def __str__(self):
        return self.nome

class Tarefa(models.Model):
    STATUS_CHOICES = [
        ('BACKLOG', 'Backlog'),
        ('A_FAZER', 'A Fazer'),
        ('EM_ANDAMENTO', 'Em Andamento'),
        ('REVISAO', 'Em Revisão'),
        ('CONCLUIDO', 'Concluído'),
    ]

    PRIORIDADE_CHOICES = [
        ('BAIXA', 'Baixa'),
        ('MEDIA', 'Média'),
        ('ALTA', 'Alta'),
    ]

    titulo = models.CharField(max_length=200, verbose_name="Título da Tarefa")
    descricao = models.TextField(verbose_name="Descrição")
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='tarefas')
    responsavel = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='tarefas_atribuidas')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='BACKLOG')
    prioridade = models.CharField(max_length=10, choices=PRIORIDADE_CHOICES, default='MEDIA')
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_entrega = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.titulo