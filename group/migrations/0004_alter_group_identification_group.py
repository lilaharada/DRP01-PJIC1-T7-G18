# Generated by Django 5.0.3 on 2024-04-24 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='identification_group',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L'), ('M', 'M'), ('N', 'N'), ('O', 'O')], max_length=1, verbose_name='Nome'),
        ),
    ]
