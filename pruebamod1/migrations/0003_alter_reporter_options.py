# Generated by Django 5.1.4 on 2025-01-24 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pruebamod1', '0002_article'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reporter',
            options={'ordering': ['first_name'], 'verbose_name': 'Reportero'},
        ),
    ]
