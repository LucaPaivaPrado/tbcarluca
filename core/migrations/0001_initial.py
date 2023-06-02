# Generated by Django 4.1.7 on 2023-03-17 00:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('endereco', models.CharField(blank=True, max_length=100, null=True, verbose_name='Endereço')),
                ('complemento', models.CharField(blank=True, max_length=50, null=True, verbose_name='Complemento')),
                ('bairro', models.CharField(blank=True, max_length=50, null=True, verbose_name='Bairro')),
                ('cidade', models.CharField(blank=True, max_length=100, null=True, verbose_name='Cidade')),
                ('fone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefone')),
                ('email', models.EmailField(max_length=100, verbose_name='E-mail')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='cliente_foto', verbose_name='Imagem')),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, verbose_name='Nome')),
                ('url', models.URLField(verbose_name='URL')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='marca_foto', verbose_name='Logo')),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=10, verbose_name='Placa')),
                ('modelo', models.CharField(blank=True, max_length=50, null=True, verbose_name='Modelo')),
                ('cor', models.CharField(blank=True, max_length=50, null=True, verbose_name='Cor')),
                ('ano', models.IntegerField(blank=True, default=2023, null=True, verbose_name='Ano')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='veiculo_foto', verbose_name='Foto')),
                ('cliente_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.cliente', verbose_name='Cliente')),
                ('marca_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.marca', verbose_name='Marca')),
            ],
        ),
    ]
