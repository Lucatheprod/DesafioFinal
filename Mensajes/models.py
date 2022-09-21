from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Room(models.Model):
    name = models.CharField(max_length=500)
class Message(models.Model):
    value = models.CharField(max_length=1500)
    data = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=15)
    room = models.CharField(max_length=1500)
