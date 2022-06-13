from django.db import models

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=100)#não permitido deixar em branco
    sub_titulo = models.CharField(max_length=200)#não permitido deixar em branco
    data_do_post = models.DateField()#não permitido deixar em branco
    conteudo = models.TextField()#não permitido deixar em branco
    conteudo_2 = models.TextField(null=True, blank=True)
    conteudo_3 = models.TextField(null=True, blank=True)
    conteudo_4 = models.TextField(null=True, blank=True)
    imagem_1 = models.ImageField(upload_to='posts')#não permitido deixar em branco
    imagem_2 = models.ImageField(upload_to='posts', null=True, blank=True)
    imagem_3 = models.ImageField(upload_to='posts', null=True, blank=True)

    def __str__(self):
        return self.titulo
