# Generated by Django 4.1.1 on 2022-09-25 22:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0012_alter_emprestimo_avaliacao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='data_emprestimo',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 25, 19, 22, 10, 742007)),
        ),
    ]
