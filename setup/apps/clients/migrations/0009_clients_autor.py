# Generated by Django 4.2.6 on 2023-12-04 19:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clients', '0008_alter_clients_city_alter_clients_uf_delete_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='clients',
            name='autor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
