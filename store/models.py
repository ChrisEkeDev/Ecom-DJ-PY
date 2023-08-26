from django.db import models

class Brand(models.Model):
    key = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    overview = models.TextField(max_length=500)

class Category(models.Model):
    key = models.CharField(max_length=10)
    name = models.CharField(max_length=100)


class Product(models.Model):
    name = models.CharField(max_length=100)
    overview = models.TextField(max_length=500)
    description = models.TextField(max_length=2000)
    price = models.IntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True);
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True);
    created_at = models.DateTimeField("date added")
