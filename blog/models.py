from django.db import models

# Create your models here.

class Blog(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    descrição = models.TextField(null=False, blank=False)
    imagem = models.TextField(null=False, blank=False)

    def __str__(self):
        return f"Blog [nome={self.nome}]"