from django.db import models

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=100)
    sub_titulo = models.CharField(max_length=200)
    data_do_post = models.DateField()
    conteudo = models.TextField()
    imagem1 = models.ImageField(upload_to='posts')
    imagem2 = models.ImageField(upload_to='posts')
    imagem3 = models.ImageField(upload_to='posts')

    def __str__(self):
        return self.titulo
