# Generated by Django 5.0.3 on 2024-05-03 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='fantasy',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Nome Fantasia'),
        ),
    ]
