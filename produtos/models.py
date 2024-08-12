from django.db import models


class Brands(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Products(models.Model):

    sku = models.CharField(max_length=50, primary_key=True)
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    price = models.FloatField()
    brand = models.ForeignKey(Brands, on_delete=models.PROTECT)

    def __str__(self):
        return self.sku