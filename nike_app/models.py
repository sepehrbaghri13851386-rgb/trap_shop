
from django.db import models

class nikies(models.Model):
    title = models.CharField(max_length=50)
    size = models.CharField(max_length=100)
    ghymat = models.DecimalField(max_digits=10, decimal_places=0)
    image = models.ImageField(upload_to='nike/')

    def __str__(self):
        return self.title

class HomeProduct(models.Model):
    CATEGORY_CHOICES = [
        ('men', 'مردانه'),
        ('women', 'زنانه'),
        ('kids', 'بچگانه'),
    ]
    title = models.CharField(max_length=50)
    size = models.CharField(max_length=100)
    ghymat = models.DecimalField(max_digits=10, decimal_places=0)
    image = models.ImageField(upload_to='home_products/')
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='men')

    def __str__(self):
        return self.title