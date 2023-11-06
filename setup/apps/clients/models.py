from django.db import models


class City(models.Model):
    name_city = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name_city
class Clients(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    company_name = models.CharField(max_length=100, unique=True)
    responsible_name = models.CharField(db_column='responsible_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cnpj_cpf = models.CharField(max_length=20, blank=True, null=True, unique=True)
    contact = models.CharField(max_length=100, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    observations = models.TextField(blank=True, null=True)
