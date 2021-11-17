from django.db import models

# Create your models here.

class upload_img(models.Model):
    image_upload=models.ImageField(upload_to='media')