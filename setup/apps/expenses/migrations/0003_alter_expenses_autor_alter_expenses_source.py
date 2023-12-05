# Generated by Django 4.2.6 on 2023-12-05 01:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0003_supplier_autor'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('expenses', '0002_rename_revenues_expenses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='autor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='expenses_autor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='source',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='expenses_source', to='supplier.supplier'),
        ),
    ]