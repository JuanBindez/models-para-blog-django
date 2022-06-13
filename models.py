from django.db import models

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=100)
    sub_titulo = models.CharField(max_length=200)
    data_do_post = models.DateField()
    conteudo = models.TextField()
    conteudo_2 = models.TextField(null=True, blank=True)
    conteudo_3 = models.TextField(null=True, blank=True)
    conteudo_4 = models.TextField(null=True, blank=True)
    imagem_1 = models.ImageField(upload_to='posts')
    imagem_2 = models.ImageField(upload_to='posts', null=True, blank=True)
    imagem_3 = models.ImageField(upload_to='posts', null=True, blank=True)

    def __str__(self):
        return self.titulo
