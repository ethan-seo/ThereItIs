from django.contrib import admin

# Register your models here.
from .models import User, Item, Transaction

admin.site.register(User)
admin.site.register(Item)
admin.site.register(Transaction)