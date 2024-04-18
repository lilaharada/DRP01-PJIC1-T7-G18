<<<<<<< HEAD
# Generated by Django 5.0.6 on 2024-05-09 18:55

import django.db.models.deletion
=======
# Generated by Django 5.0.3 on 2024-04-18 19:09

import django.db.models.deletion
from django.conf import settings
>>>>>>> ee2e9db (add, configurate and edit app teacher)
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
<<<<<<< HEAD
        ('core', '0001_initial'),
        ('school', '0004_alter_classroom_classroom_tyoe_academicyear'),
=======
        ('school', '0003_structschool'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
>>>>>>> ee2e9db (add, configurate and edit app teacher)
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('first_name', models.CharField(max_length=20, verbose_name='Nome')),
                ('last_name', models.CharField(max_length=70, verbose_name='Sobrenome')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='school.school', verbose_name='Escola')),
            ],
            options={
                'verbose_name': 'Professor(a)',
                'verbose_name_plural': 'Professore(a)s',
            },
        ),
        migrations.CreateModel(
            name='PhoneTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_code', models.IntegerField(verbose_name='Código do Pais')),
                ('locale_code', models.IntegerField(verbose_name='Código da Localidade')),
                ('number', models.IntegerField(verbose_name='Numero')),
                ('phone_type', models.CharField(choices=[('C', 'Celular'), ('P', 'Principal'), ('W', 'Whatsapp'), ('T', 'Telegran'), ('O', 'Outro')], default='P', max_length=1)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher', verbose_name='Professor')),
            ],
            options={
                'verbose_name': 'Telefone do Professor(a)',
                'verbose_name_plural': 'Telefones do Professor(a)',
            },
        ),
        migrations.CreateModel(
            name='AddressTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(verbose_name='Número')),
                ('complement', models.CharField(blank=True, max_length=20, null=True, verbose_name='Complemento')),
                ('zipcode', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='core.address', verbose_name='CEP')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher', verbose_name='Professor')),
            ],
            options={
                'verbose_name': 'Endereço do Professor(a)',
                'verbose_name_plural': 'Endereços do Professor(a)',
=======
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('first_name', models.CharField(max_length=50, verbose_name='Primeiro Nome')),
                ('last_name', models.CharField(max_length=70, verbose_name='Sobrenome')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('phone_ddd', models.CharField(max_length=4, verbose_name='DDD')),
                ('phone_number', models.CharField(max_length=9, verbose_name='Telefone')),
                ('address_zipcode', models.CharField(max_length=9, verbose_name='CEP')),
                ('address', models.CharField(max_length=150, verbose_name='Endereço')),
                ('address_number', models.CharField(max_length=5, verbose_name='Número')),
                ('address_complement', models.CharField(max_length=20, verbose_name='Complemento')),
                ('address_district', models.CharField(max_length=50, verbose_name='Bairro')),
                ('address_city', models.CharField(max_length=70, verbose_name='Cidade')),
                ('address_state', models.CharField(max_length=2, verbose_name='UF')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school.school', verbose_name='Escola')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Professor',
                'verbose_name_plural': 'Professores',
>>>>>>> ee2e9db (add, configurate and edit app teacher)
            },
        ),
    ]
