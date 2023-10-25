from django.db import models


class Clients(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    company_name = models.CharField(max_length=100, db_collation='Latin1_General_CI_AS')
    responsible_name = models.CharField(db_column='responsible_name', max_length=50, db_collation='Latin1_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cnpj_cpf = models.CharField(max_length=20, db_collation='Latin1_General_CI_AS', blank=True, null=True)
    contact = models.CharField(max_length=100, db_collation='Latin1_General_CI_AS', blank=True, null=True)
    city = models.CharField(max_length=50, db_collation='Latin1_General_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Clientes'
