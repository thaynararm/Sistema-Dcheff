# Generated by Django 4.2.6 on 2023-11-06 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0007_alter_clients_cnpj_cpf'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='uf_city',
            field=models.CharField(default='null', max_length=5),
        ),
    ]
