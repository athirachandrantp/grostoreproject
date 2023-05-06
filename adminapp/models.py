from django.db import models

# Create your models here.

class products_upload(models.Model):
    category_choices = [
    ("grocery", "grocery"),
    ("vegetables" ,"vegetables"),
    ("fruits", "fruits"),
    ("chocolates" ,"chocolates"),
]
    product_title = models.TextField(max_length=50)
    product_category = models.CharField(max_length=50, choices=category_choices, default='grocery', null=True)
    product_quantity = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    product_price = models.DecimalField(max_digits=50, decimal_places=3, null=True)
    product_description = models.TextField(max_length=50)
    product_image = models.ImageField(upload_to='profile/')

class admin_registration(models.Model):
    adminname = models.TextField(max_length=50)
    adminaddress = models.TextField(max_length=50)
    admincontact = models.TextField(max_length=50)
    adminusername = models.TextField(max_length=50)
    adminpassword = models.TextField(max_length=50)
    adminconfirmpassword = models.TextField(max_length=50)





    
