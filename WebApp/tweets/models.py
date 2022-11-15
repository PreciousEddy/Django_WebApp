from django.db import models

# Create your models here.

class Tweets (models.Model): # defining a class tweets
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')


    def __str__(self):
        return self.title
