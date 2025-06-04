from django.db import models

class Ficha(models.Model):
    nome = models.CharField(max_length=100)
    classe = models.CharField(max_length=50)
    raca = models.CharField(max_length=50)
    nivel = models.IntegerField(default=1)
    forca = models.IntegerField(default=10)
    destreza = models.IntegerField(default=10)
    constituicao = models.IntegerField(default=10)
    inteligencia = models.IntegerField(default=10)
    sabedoria = models.IntegerField(default=10)
    carisma = models.IntegerField(default=10)

    def __str__(self):
        return self.nome
