from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.


class Product(models.Model):
    # id = models.AutoField()
    # keeps all associates
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    # user = models.ForeignKey(User, null=True, on_delete=models.CASCADE) # deletes all associates
    title = models.CharField(max_length=220)
    desc = models.TextField(null=True, blank=True,
                            default="Details coming soon")
    price = models.FloatField()
