from django.db import models

# Create your models here.
class Category(models.Model):
    objects = models.Model
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name
class Product(models.Model):
    objects = models.Model
    name = models.CharField(max_length=50)
    descreption = models.CharField(max_length=255)
    product_amount = models.IntegerField()
    price = models.FloatField()
    reviews = models.FloatField()
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to='images/', default=None, null=True, blank=True)

    def __str__(self):
        return self.name

class UserCart(models.Model):
    objects = models.Model
    user_id = models.IntegerField()
    user_product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True   )
    user_product_quantity = models.IntegerField()
    added_date = models.DateTimeField(auto_now_add=True)





