from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    code = models.IntegerField(unique=True)
    is_active = models.BooleanField(default=True)
    quantity_in_stock = models.IntegerField()
    seller = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Products"

