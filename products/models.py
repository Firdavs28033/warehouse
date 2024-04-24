from django.db import models
from users.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    INN = models.IntegerField(default=0)
    contact_number = models.CharField(max_length=11)

    def __str__(self):
        return self.name

class Product(models.Model):
    inn_code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveIntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateField(null=True, blank=True)
    brand = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to='products/', default="cover_pic/nopicture.png")

    def __str__(self):
        return self.name



class QRCode(models.Model):
    url = models.TextField()

    def __str__(self):
        return f"QRCode {self.id}"
