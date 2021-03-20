from django.db import models


class Post(models.Model):
    username = models.CharField(max_length=70)
    foodimage = models.ImageField(upload_to='images/')
