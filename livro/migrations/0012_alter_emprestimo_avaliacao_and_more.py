# Generated by Django 4.1.1 on 2022-09-25 15:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_alter_usuario_senha'),
        ('livro', '0011_emprestimo_avaliacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='avaliacao',
            field=models.CharField(blank=True, choices=[('P', 'Péssimo'), ('R', 'Ruim'), ('B', 'Bom'), ('O', 'Ótimo')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='data_devolucao',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='data_emprestimo',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 25, 12, 31, 44, 196448)),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='nome_emprestado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.usuario'),
        ),
    ]
