from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True

class Product(BaseModel):
    brand = models.CharField(max_length=200, null=False)
    description = models.TextField(max_length=500, null=False)
    img_url = models.CharField(max_length=200, null=False)
    rating = models.FloatField(null=True)
    price = models.IntegerField(null=False)
    actual_price = models.IntegerField(null=False)
    discount = models.FloatField(default=0)
    color = models.CharField(max_length=100)
