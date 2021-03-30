from django.db import models

class category(models.Model):
    category = models.CharField(max_length=20)
    Descryption = models.CharField(max_length=300)
    Business_Web = models.URLField(max_length = 200)
    photo = models.ImageField(upload_to='media/Business_Detail/images')