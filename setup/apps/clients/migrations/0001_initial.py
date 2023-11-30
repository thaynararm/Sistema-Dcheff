# Generated by Django 4.2.6 on 2023-11-22 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_city', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uf', models.CharField(max_length=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100, unique=True)),
                ('responsible_name', models.CharField(blank=True, db_column='responsible_name', max_length=50, null=True)),
                ('cnpj_cpf', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('contact', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('observations', models.TextField(blank=True, null=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.city')),
                ('uf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.states')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='uf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.states'),
        ),
    ]
