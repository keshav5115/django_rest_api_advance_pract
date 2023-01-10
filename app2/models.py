from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Customer(models.Model):
    cname = models.CharField(max_length=30 )
    mob=models.PositiveBigIntegerField()
    email = models.EmailField()
    loc=models.CharField(max_length=40)

    def __str__(self):
        return self.cname


class Products(models.Model):
    pname=models.CharField(max_length=20)
    qty=models.IntegerField()
    active=models.BooleanField(default=True)
    created=models.DateField(auto_now_add=True,null=True)
    customer=models.ManyToManyField(Customer,related_name='products')
    def __str__(self):
        return self.pname


class Review(models.Model):
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    description=models.CharField(max_length=200)
    product=models.ForeignKey(Products,related_name='reviews',on_delete=models.CASCADE)
    active=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.rating) + '-' + self.product.pname