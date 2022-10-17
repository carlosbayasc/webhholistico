from django.db import models

# Create your models here.
class Elybra(models.Model):
    titulo=models.CharField(max_length=200,verbose_name="Titulo")
    subtitulo1 = models.CharField(verbose_name="SubTitulo1", max_length=50)
    contenido1= models.TextField(verbose_name="Contenido1", max_length=150)
    subcontenido1= models.TextField(verbose_name="SubContenido1", max_length=150)
    subtitulo2 = models.CharField(verbose_name="SubTitulo2", max_length=50)
    contenido2 = models.TextField(verbose_name="Contenido2", max_length=150)
    subcontenido2 = models.TextField(verbose_name="SubContenido2", max_length=150)
    subtitulo3 = models.CharField(verbose_name="SubTitulo3", max_length=50)   
    contenido3 = models.TextField(verbose_name="Contenido3", max_length=150)   
    subcontenido3 = models.TextField(verbose_name="SubContenido3", max_length=150)
    pie1 = models.CharField(max_length=50)
    detPie1 = models.TextField( max_length=50)
    pie2 = models.CharField(max_length=50)
    detPie2 = models.TextField( max_length=50)
    pie3 = models.CharField( max_length=50)
    detPie3 = models.TextField( max_length=50)
    pie4 = models.CharField( max_length=50)    
    detPie4 = models.TextField( max_length=50)
    created= models.DateField( auto_now=False, auto_now_add=True)
    updated= models.DateField( auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return self.titulo



