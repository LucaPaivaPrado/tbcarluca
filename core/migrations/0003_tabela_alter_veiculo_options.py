# Generated by Django 4.1.7 on 2023-04-14 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_marca_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tabela',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50, verbose_name='Descrição')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Valor')),
            ],
            options={
                'verbose_name_plural': 'Tabelas',
            },
        ),
        migrations.AlterModelOptions(
            name='veiculo',
            options={'verbose_name_plural': 'Veículos'},
        ),
    ]
