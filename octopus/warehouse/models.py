from django.db import models
from django.conf import settings


class Products(models.Model):
    name = models.CharField(max_length=255)
    bar_code = models.CharField(max_length=255)
    qtt = models.IntegerField(default= 0)
    img= models.ImageField()

    def __str__(self):
        return f'{self.name} ({self.qtt})'


class Sails(models.Model):
    bar_code = models.CharField(max_length=255)
    qtt = models.IntegerField(default=0)
    id_ML = models.CharField(max_length=255)

    def __str__(self):
        return f'"{self.id_ML}" - {self.bar_code}: {self.qtt}'

class Employees(models.Model):
    id_e= models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    img_e= models.ImageField()

    def __str__(self):
        return f'"{self.name}" - {self.position}. Senha: {self.password}'

class Inventory(models.Model):
    sail = models.ForeignKey(Sails, on_delete=models.CASCADE, null= True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    qtt= models.IntegerField(default=0)
    mov= models.CharField(max_length= 255)
    date = models.DateTimeField(auto_now= True)

    def __str__(self):
        return f'"Código de venda nº {self.sail}" do produto {self.product} feita pelo funcionário {self.employee} em {self.date}'
