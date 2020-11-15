from __future__ import unicode_literals
from django.db import models
import re

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
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.CharField(max_length=50)
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

LOCATION_CHOICES = (("CA","CA"),("OH","OH"),("WA","WA"))

class Item(models.Model):
    sku = models.CharField(max_length=50)
    productname = models.CharField(max_length=50)
    productdesc = models.TextField()
    quanity = models.IntegerField()
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES,blank=True)
    expiration_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

TRANSACTION_TYPE = (("ADD","ADD"),("REMOVE","REMOVE"))

class Transaction(models.Model):
    notes = models.CharField(max_length=255,blank=True, null=True)
    transaction_type = models.CharField(max_length=50, choices=TRANSACTION_TYPE,blank=True)
    update_user = models.ForeignKey(User, related_name='transaction_user', on_delete=models.CASCADE)
    updated_item = models.ForeignKey(Item, related_name="transaction_item", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
