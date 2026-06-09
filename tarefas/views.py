from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Tarefa, Projeto, Departamento, PerfilUsuario
from django.contrib.auth.models import User


@login_required
def dashboard(request):
    """Dashboard com visão Kanban das tarefas"""
    tarefas_backlog = Tarefa.objects.filter(status='BACKLOG')
    tarefas_a_fazer = Tarefa.objects.filter(status='A_FAZER')
    tarefas_em_andamento = Tarefa.objects.filter(status='EM_ANDAMENTO')
    tarefas_revisao = Tarefa.objects.filter(status='REVISAO')
    tarefas_concluidas = Tarefa.objects.filter(status='CONCLUIDO')
    
    total_tarefas = Tarefa.objects.count()
    tarefas_concluidas_count = tarefas_concluidas.count()
    
    context = {
        'tarefas_backlog': tarefas_backlog,
        'tarefas_a_fazer': tarefas_a_fazer,
        'tarefas_em_andamento': tarefas_em_andamento,
        'tarefas_revisao': tarefas_revisao,
        'tarefas_concluidas': tarefas_concluidas,
        'total_tarefas': total_tarefas,
        'tarefas_concluidas_count': tarefas_concluidas_count,
    }
    return render(request, 'tarefas/dashboard.html', context)


@login_required
def lista_tarefas(request):
    """Lista todas as tarefas com filtros"""
    tarefas = Tarefa.objects.all().order_by('-data_criacao')
    
    # Filtros
    status_filter = request.GET.get('status')
    prioridade_filter = request.GET.get('prioridade')
    projeto_filter = request.GET.get('projeto')
    
    if status_filter:
        tarefas = tarefas.filter(status=status_filter)
    if prioridade_filter:
        tarefas = tarefas.filter(prioridade=prioridade_filter)
    if projeto_filter:
        tarefas = tarefas.filter(projeto_id=projeto_filter)
    
    projetos = Projeto.objects.all()
    
    context = {
        'tarefas': tarefas,
        'projetos': projetos,
        'status_choices': Tarefa.STATUS_CHOICES,
        'prioridade_choices': Tarefa.PRIORIDADE_CHOICES,
    }
    return render(request, 'tarefas/lista_tarefas.html', context)


@login_required
def detalhe_tarefa(request, pk):
    """Detalhes de uma tarefa"""
    tarefa = get_object_or_404(Tarefa, pk=pk)
    context = {'tarefa': tarefa}
    return render(request, 'tarefas/detalhe_tarefa.html', context)


@login_required
def criar_tarefa(request):
    """Criar nova tarefa"""
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        projeto_id = request.POST.get('projeto')
        prioridade = request.POST.get('prioridade')
        responsavel_id = request.POST.get('responsavel')
        data_entrega = request.POST.get('data_entrega')
        
        projeto = Projeto.objects.get(id=projeto_id)
        responsavel = User.objects.get(id=responsavel_id) if responsavel_id else None
        
        Tarefa.objects.create(
            titulo=titulo,
            descricao=descricao,
            projeto=projeto,
            prioridade=prioridade,
            responsavel=responsavel,
            data_entrega=data_entrega if data_entrega else None,
            status='BACKLOG'
        )
        return redirect('dashboard')
    
    projetos = Projeto.objects.all()
    usuarios = User.objects.all()
    
    context = {
        'projetos': projetos,
        'usuarios': usuarios,
        'prioridade_choices': Tarefa.PRIORIDADE_CHOICES,
    }
    return render(request, 'tarefas/criar_tarefa.html', context)


@login_required
def editar_tarefa(request, pk):
    """Editar tarefa existente"""
    tarefa = get_object_or_404(Tarefa, pk=pk)
    
    if request.method == 'POST':
        tarefa.titulo = request.POST.get('titulo')
        tarefa.descricao = request.POST.get('descricao')
        tarefa.prioridade = request.POST.get('prioridade')
        tarefa.status = request.POST.get('status')
        responsavel_id = request.POST.get('responsavel')
        data_entrega = request.POST.get('data_entrega')
        
        if responsavel_id:
            tarefa.responsavel = User.objects.get(id=responsavel_id)
        
        if data_entrega:
            tarefa.data_entrega = data_entrega
        
        tarefa.save()
        return redirect('detalhe_tarefa', pk=tarefa.id)
    
    usuarios = User.objects.all()
    context = {
        'tarefa': tarefa,
        'usuarios': usuarios,
        'status_choices': Tarefa.STATUS_CHOICES,
        'prioridade_choices': Tarefa.PRIORIDADE_CHOICES,
    }
    return render(request, 'tarefas/editar_tarefa.html', context)


@login_required
def deletar_tarefa(request, pk):
    """Deletar tarefa"""
    tarefa = get_object_or_404(Tarefa, pk=pk)
    
    if request.method == 'POST':
        tarefa.delete()
        return redirect('dashboard')
    
    context = {'tarefa': tarefa}
    return render(request, 'tarefas/confirmar_deletar.html', context)


@login_required
def lista_projetos(request):
    """Lista de projetos"""
    projetos = Projeto.objects.all()
    context = {'projetos': projetos}
    return render(request, 'tarefas/lista_projetos.html', context)


@login_required
def detalhe_projeto(request, pk):
    """Detalhes do projeto e suas tarefas"""
    projeto = get_object_or_404(Projeto, pk=pk)
    tarefas = projeto.tarefas.all()
    
    context = {
        'projeto': projeto,
        'tarefas': tarefas,
    }
    return render(request, 'tarefas/detalhe_projeto.html', context)
