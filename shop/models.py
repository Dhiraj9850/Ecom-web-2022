from django.db import models

# Create your models here.
class Product(models.Model):
    Product_id = models.AutoField(primary_key=True)
    Product_name = models.CharField(max_length=30)
    product_weight = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    create_date = models.DateField()
    update_date = models.DateField()
    image = models.ImageField(upload_to="shop/images",default= " ")

def __str__(self):
    return self.product_name
