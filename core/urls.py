from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from tarefas import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('tarefas/', views.lista_tarefas, name='lista_tarefas'),
    path('tarefas/criar/', views.criar_tarefa, name='criar_tarefa'),
    path('tarefas/<int:pk>/', views.detalhe_tarefa, name='detalhe_tarefa'),
    path('tarefas/<int:pk>/editar/', views.editar_tarefa, name='editar_tarefa'),
    path('tarefas/<int:pk>/deletar/', views.deletar_tarefa, name='deletar_tarefa'),
    path('tarefas/<int:pk>/status/', views.atualizar_status, name='atualizar_status'),
    path('projetos/', views.lista_projetos, name='lista_projetos'),
    path('projetos/<int:pk>/', views.detalhe_projeto, name='detalhe_projeto'),
    path('login/', auth_views.LoginView.as_view(template_name='tarefas/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
]
