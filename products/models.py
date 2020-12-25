from django.db import models

# Create your models here.


class Product(models.Model):
    # id = models.AutoField()
    title = models.CharField(max_length=220)
    desc = models.TextField(null=True, blank=True,
                            default="Details coming soon")
    price = models.FloatField()
