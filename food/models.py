from django.db import models


class Post(models.Model):
    foodimage = models.ImageField(upload_to='images/')
