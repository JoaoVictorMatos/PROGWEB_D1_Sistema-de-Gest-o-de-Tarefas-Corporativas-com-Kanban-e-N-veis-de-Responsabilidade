from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfilusuario',
            name='nivel_responsabilidade',
            field=models.CharField(
                choices=[
                    ('COLABORADOR', 'Colaborador'),
                    ('LIDER', 'Líder de Equipe'),
                    ('GERENTE', 'Gerente'),
                    ('DIRETOR', 'Diretor'),
                ],
                default='COLABORADOR',
                max_length=20,
                verbose_name='Nível de Responsabilidade',
            ),
        ),
    ]
