from django.db import models

class Mobile(models.Model):
    phone = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    ram = models.CharField(max_length=50)
    memory = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    img_url = models.URLField(max_length=50)

    def __str__(self):
        return self.name