#!/bin/bash
# Script para configurar e executar o projeto Django com Admin customizado

echo "=========================================="
echo "Configurando Django - Admin Customizado"
echo "=========================================="
echo ""

# 1. Coletar arquivos estáticos
echo "1️⃣  Coletando arquivos estáticos..."
python manage.py collectstatic --noinput --clear

echo ""
echo "2️⃣  Aplicando migrações..."
python manage.py migrate

echo ""
echo "=========================================="
echo "✅ Configuração concluída!"
echo "=========================================="
echo ""
echo "Para iniciar o servidor, execute:"
echo "   python manage.py runserver"
echo ""
echo "Para acessar o admin:"
echo "   http://localhost:8000/admin/"
echo ""
