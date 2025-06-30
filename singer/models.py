from django.db import models

# Create your models here.
class Singer(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    debut = models.DateTimeField()

class Song(models.Model):
    id = models.AutoField(primary_key=True)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name = 'songs')
    release = models.DateTimeField()
    content = models.TextField()