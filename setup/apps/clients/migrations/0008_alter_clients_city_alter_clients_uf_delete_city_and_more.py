# Generated by Django 4.2.6 on 2023-11-30 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0002_alter_supplier_city_alter_supplier_uf'),
        ('clients', '0007_alter_clients_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='uf',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='States',
        ),
    ]
