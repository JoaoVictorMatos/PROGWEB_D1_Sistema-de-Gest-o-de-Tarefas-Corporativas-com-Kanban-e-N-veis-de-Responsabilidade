@echo off
cd /d "C:\Users\João\Desktop\projetos\PROGWEB_D1_Sistema-de-Gest-o-de-Tarefas-Corporativas-com-Kanban-e-N-veis-de-Responsabilidade"

echo.
echo ========================================
echo  Iniciando Django + Admin Customizado
echo ========================================
echo.
echo Acessar em: http://localhost:8000/admin/
echo.
echo Pressione CTRL+C para parar o servidor
echo.

python manage.py runserver 0.0.0.0:8000
