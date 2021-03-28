from django.db import models
from phone_field import PhoneField

# Create your models here.
class UserManagementSystem(models.Model):
    name = models.CharField(max_length = 150)
    emailId = models.EmailField(max_length = 254)
    contactno = PhoneField(blank=False, unique=True)
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 150)
    confirmpassword = models.CharField(max_length = 150)

    def __str__(self):
        return self.username

class ClientManagementSystem(models.Model):
    name = models.CharField(max_length = 150)
    emailId = models.EmailField(max_length = 254)
    phno = PhoneField(blank=False, unique=True)
    clientid = models.CharField(max_length = 50, unique=True)
    address = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.clientid

class DeviceInfo(models.Model):
    deviceid = models.ForeignKey(ClientManagementSystem,to_field='clientid',on_delete=models.CASCADE)
    macaddress = models.CharField(max_length = 12)

    def __str__(self):
        return self.deviceid
