from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class formi(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=50)

    discribshen = models.TextField()

    images = models.ImageField(upload_to='images/formies')

    my_call = models.CharField(max_length=12,null=True,blank=True)

    zaman = models.DateField(default=timezone.now)

    Published = models.BooleanField(default=True)
    slog = models.SlugField(null=True,unique=True)
class CartItem(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(formi,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def str(self):
        return f"{self.user.username} - {self.product.title}"

    def str(self):
        return self.title