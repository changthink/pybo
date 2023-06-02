from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_photos')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default='photos/no_image.png')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return self.author.username+" "+self.created.strftime("%Y-%m-%d %H:%M:%S")

    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=[self.id])


class Brand(models.Model):
    brand = models.CharField(max_length=30, null=True, blank=True)
    desc = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.brand

class Unit(models.Model):
    name = models.ForeignKey(Brand, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, null=True, blank=True)
    img = models.ImageField()

    def __str__(self):
        return self.type


class Viewimage(models.Model):
    pj = models.CharField(max_length=30, null=True, blank=True)
    view_img = models.ImageField()

    def __str__(self):
        return self.pj