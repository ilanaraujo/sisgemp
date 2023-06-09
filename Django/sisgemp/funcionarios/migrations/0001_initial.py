# Generated by Django 4.2 on 2023-04-11 23:46

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departamentos', '0002_alter_departamento_data_atualizacao_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sexo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('sexo', models.CharField(max_length=9, unique=True)),
                ('data_criacao', models.DateTimeField(default=datetime.datetime(2023, 4, 11, 23, 46, 44, 916861))),
                ('data_atualizacao', models.DateTimeField(default=datetime.datetime(2023, 4, 11, 23, 46, 44, 916905))),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50, unique=True)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('rg', models.CharField(max_length=9, unique=True)),
                ('nascimento', models.DateField()),
                ('possui_cnh', models.BooleanField()),
                ('salario', models.FloatField()),
                ('carga_horaria_semanal', models.IntegerField()),
                ('horas_livres', models.IntegerField()),
                ('data_criacao', models.DateTimeField(default=datetime.datetime(2023, 4, 11, 23, 46, 44, 918612))),
                ('data_atualizacao', models.DateTimeField(default=datetime.datetime(2023, 4, 11, 23, 46, 44, 918649))),
                ('departamento_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departamentos.departamento')),
                ('sexo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='funcionarios.sexo')),
            ],
        ),
    ]
