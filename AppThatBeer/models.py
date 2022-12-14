import datetime

from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    direccion = models.CharField(max_length=60)
    provincia = models.CharField(max_length=25)
    cp = models.IntegerField()
    dni = models.IntegerField(unique=True)
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
class Distribuidor(models.Model):
    nombre = models.CharField(max_length=30)
    cuit = models.IntegerField()
    direccion = models.CharField(max_length=45)
    provincia = models.CharField(max_length=25)
    descuento = models.IntegerField()
    web = models.URLField()
    def __str__(self):
        return self.nombre
class Producto(models.Model):
    nombre = models.CharField(max_length=35)
    variedad = models.CharField(max_length=20)
    contenido_ml = models.IntegerField()
    codigo = models.CharField(unique=True, max_length=10)
    descripcion = models.CharField(max_length=150)
    def __str__(self):
        return f'{self.codigo}'
class Patrocinador(models.Model):
    nombre= models.CharField(max_length=15)
    rubro = models.CharField(max_length=30)
    slogan = models.CharField(max_length=100)
    antiguedad_anios = models.IntegerField()
    web = models.URLField(unique=True)
    def __str__(self):
        return f'{self.nombre}'

class Noticia(models.Model):
    titulo = models.CharField(max_length=45)
    subtitulo = models.CharField(max_length=35)
    cuerpo = models.CharField(max_length=3000)
    autor = models.CharField(max_length=25)
    imagen = models.ImageField(upload_to='noticiasimg')
    fecha_posteo = models.DateField()
    def __str__(self):
        return f'{self.titulo}'
    
#    titulo = models.CharField(max_length=45)
#    subtitulo = models.CharField(max_length=35)
#    cuerpo = RichTextField(blank=True, null = True)
#    autor = models.CharField(max_length=25)
#    imagen = models.ImageField(upload_to='noticiasimg', null=True, blank=True)
#    fecha_posteo = models.DateField()