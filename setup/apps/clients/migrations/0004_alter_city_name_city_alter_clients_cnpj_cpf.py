# Generated by Django 4.2.6 on 2023-11-22 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_alter_clients_cnpj_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name_city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='clients',
            name='cnpj_cpf',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
    ]
