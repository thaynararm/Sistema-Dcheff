# Generated by Django 4.2.6 on 2023-12-05 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_code',
            field=models.DateField(unique=True),
        ),
    ]
