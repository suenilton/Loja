# Generated by Django 4.0.4 on 2022-06-03 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roupas', '0002_produto_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='slug',
        ),
    ]