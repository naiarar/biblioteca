# Generated by Django 4.1.1 on 2022-09-26 15:02

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0015_livros_image_alter_emprestimo_data_emprestimo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='data_emprestimo',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 26, 12, 2, 35, 998198)),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='livro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livro.livros'),
        ),
    ]
