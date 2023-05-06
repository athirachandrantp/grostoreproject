from django.db import models

# Create your models here.

class users_registration(models.Model):
    username = models.TextField(max_length=50)
    useraddress = models.TextField(max_length=50)
    usernumber = models.TextField(max_length=50)
    userdateofbirth = models.DateField(null=True)
    userusername = models.TextField(max_length=50)
    userpassword = models.TextField(max_length=50)
    userconfirmpassword = models.TextField(max_length=50)



