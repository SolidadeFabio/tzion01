from django.db import models


class Supplier(models.Model):
    cnpj = models.CharField(max_length=14)
    name = models.CharField(max_length=80)