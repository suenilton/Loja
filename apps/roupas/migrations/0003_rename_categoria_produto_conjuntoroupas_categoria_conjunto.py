# Generated by Django 4.0.4 on 2022-05-27 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roupas', '0002_conjuntoroupas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conjuntoroupas',
            old_name='categoria_produto',
            new_name='categoria_conjunto',
        ),
    ]
