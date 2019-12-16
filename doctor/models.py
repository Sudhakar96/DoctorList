from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Doctor(models.Model):
    full_name= models.CharField(max_length=100)
    d_id = models.CharField(max_length=3)
    contact= models.CharField(max_length=15)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    
