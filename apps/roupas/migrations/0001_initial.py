# Generated by Django 4.0.4 on 2022-06-02 18:32

import autoslug.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('nome_categoria', models.CharField(max_length=255, unique=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='nome_categoria', unique=True)),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorias',
                'ordering': ('nome_categoria',),
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_produto', models.CharField(max_length=200)),
                ('preco_produto', models.CharField(max_length=20)),
                ('marca_produto', models.CharField(blank=True, max_length=100)),
                ('descricao_produto', models.CharField(max_length=200)),
                ('tamanho_produto', models.CharField(choices=[('P', 'Pequeno'), ('M', 'Médio'), ('G', 'Grande')], max_length=1)),
                ('img_produto', models.ImageField(blank=True, upload_to='fotos\\%d\\%m\\%Y')),
                ('data_produto', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('status_produto', models.BooleanField(default=False, verbose_name='publicado')),
                ('categoria_produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produtos', to='roupas.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='ConjuntoRoupas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_conjunto', models.CharField(choices=[('1', 'imagem 01'), ('2', 'imagem 02'), ('3', 'imagem 03'), ('4', 'imagem 04')], default=None, max_length=1)),
                ('nome_conjunto', models.CharField(max_length=200)),
                ('preco_conjunto', models.CharField(max_length=20)),
                ('descricao_conjunto', models.CharField(max_length=200)),
                ('categoria_conjunto', models.CharField(max_length=100)),
                ('img_conjunto', models.ImageField(blank=True, upload_to='fotos\\%d\\%m\\%Y')),
                ('data_conjunto', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('status_conjunto', models.BooleanField(default=False, verbose_name='publicado')),
                ('nome_produtos_do_conjunto', models.ManyToManyField(related_name='conjuntos', to='roupas.produto')),
            ],
        ),
    ]
