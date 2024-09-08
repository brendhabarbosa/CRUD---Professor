from django.db import models

# Create your models here.
class Area(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    email = models.EmailField()
    endereço = models.CharField(max_length=250)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome
