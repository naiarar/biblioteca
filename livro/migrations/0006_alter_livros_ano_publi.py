# Generated by Django 4.1.1 on 2022-09-13 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0005_livros_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livros',
            name='ano_publi',
            field=models.DateField(),
        ),
    ]
