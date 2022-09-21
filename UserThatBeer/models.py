from django.contrib.auth.models import User, AbstractBaseUser
from django.db import models



class Avatar(models.Model):
    # referencia uno a uno
    # Al eliminar el usuario se elimina por 'cascada' el avatar
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
    
class Profile(models.Model):
    user = models.OneToOneField(User, null = True, on_delete=models.CASCADE)
    bio = models.TextField(max_length=350)
    avatar = Avatar.imagen
    def __str__(self):
        return str(self.user)

