from __future__ import unicode_literals
from django.db import models
import re
from django.core.files.storage import FileSystemStorage
from django.conf import settings

# Create your models here.
class UserManager(models.Manager):
    def create_validator(self, reqPOST):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(reqPOST['first_name']) == 0 or len(reqPOST['last_name']) == 0 or len(reqPOST["email"]) == 0 or len(reqPOST['password']) == 0 or len(reqPOST['password_conf']) == 0:
            errors["req_fields"] = "All Fields are required"
        if len(reqPOST['first_name']) < 2:
            errors["first_name"] = "First name should be at least 2 characters"
        if len(reqPOST['last_name']) < 2:
            errors["last_name"] = "Last name should be at least 2 characters"
        if len(reqPOST['password']) < 8:
            errors['password'] = "Passwords must be at least 8 characters"
        if reqPOST['password'] != reqPOST['password_conf']:
            errors['password_conf'] = "Passwords need to match"
        email_check = self.filter(email=reqPOST['email'])
        if email_check:
            errors['email'] = "Email already in use"    
        if not EMAIL_REGEX.match(reqPOST["email"]):
            errors['regex'] = "Email is not in correct format"
        return errors
    
    def login_validator(self, reqPOST):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(reqPOST["email"]) == 0 or len(reqPOST['password']) == 0:
            errors["req_fields"] = "All Fields are required"
        if not EMAIL_REGEX.match(reqPOST["email"]):
            errors['regex'] = "Email is not in correct format"
        email_check = self.filter(email = reqPOST['email'])
        if len(email_check)==0:
            errors['email'] = "Account does not exist!"
        return errors

    def update_validator(self, reqPOST):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(reqPOST["email"]):
            errors['regex'] = "Email is not in correct format"
        email_check = self.filter(email = reqPOST['email'])
        if len(email_check)==0:
            errors['email'] = "Account does not exist!"
        if len(reqPOST['first_name']) < 2:
            errors["first_name"] = "First name should be at least 2 characters"
        if len(reqPOST['last_name']) < 2:
            errors["last_name"] = "Last name should be at least 2 characters"
        if len(reqPOST['password']) < 8:
            errors['password'] = "Passwords must be at least 8 characters"
        if reqPOST['password'] != reqPOST['password_conf']:
            errors['password_conf'] = "Passwords need to match"
        return errors

# image_storage = FileSystemStorage(
#     # Physical file location ROOT
#     location=u'{0}/'.format(settings.MEDIA_ROOT),
#     # Url for file
#     base_url=u'{0}/'.format(settings.MEDIA_URL),
# )

# def image_directory_path(instance, filename):
#     # file will be uploaded to MEDIA_ROOT/ThereItIs_app/static/media/<filename>
#     # return u'media/{0}'.format(filename)
#     return u'ThereItIs_app/static/media/{0}'.format(filename)

class User(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.CharField(max_length=50)
    password = models.TextField()
    profile_image = models.ImageField(upload_to='ThereItIs_app/static/media', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        return self.first_name + self.last_name 

LOCATION_CHOICES = (("CA","CA"),("OH","OH"),("WA","WA"))

class Item(models.Model):
    sku = models.CharField(max_length=50)
    productname = models.CharField(max_length=50)
    productdesc = models.TextField()
    quantity = models.IntegerField()
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES,blank=True)
    expiration_date = models.DateTimeField(blank=True, null=True)
    mainimage = models.ImageField(upload_to='ThereItIs_app/static/media/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.productname

TRANSACTION_TYPE = (("Add New Item","Add New Item"),("Add Stock","Add Stock"),("Remove","Remove"))

class Transaction(models.Model):
    notes = models.CharField(max_length=255,blank=True, null=True)
    transaction_type = models.CharField(max_length=50, choices=TRANSACTION_TYPE,blank=True)
    item_sku = models.CharField(max_length=50, blank=True)
    item_name = models.CharField(max_length=50, blank=True)
    update_user = models.ForeignKey(User, related_name='transaction_user', on_delete=models.CASCADE)
    updated_item = models.ForeignKey(Item, related_name="transaction_item", null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item_name + "_" + self.transaction_type
