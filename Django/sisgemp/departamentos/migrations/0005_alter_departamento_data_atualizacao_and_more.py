# Generated by Django 4.2 on 2023-04-13 05:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamentos', '0004_alter_departamento_data_atualizacao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='data_atualizacao',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 13, 5, 34, 30, 492719)),
        ),
        migrations.AlterField(
            model_name='departamento',
            name='data_criacao',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 13, 5, 34, 30, 492705)),
        ),
    ]