from django.db import models

# Create your models here.

class Trainee (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=100, unique=True, null=False)
    image = models.ImageField(upload_to='trainees/images/')
