from django.db import models

# Create your models here.
class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

def image_upload_path(instance, filename):
    return f'{instance.pk}/{filename}'

class Singer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default='임시이름')
    genre = models.CharField(max_length=50, default='기타')
    member_count = models.IntegerField(default='1')
    content = models.TextField()
    debut = models.DateTimeField()
    tags = models.ManyToManyField(Tag, blank=True)

class SingerImage(models.Model):
    singer = models.ForeignKey(Singer, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='singer_images/')


class Song(models.Model):
    id = models.AutoField(primary_key=True)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name = 'songs')
    title = models.CharField(max_length=100, default='임시제목')
    release = models.DateTimeField()
    content = models.TextField()