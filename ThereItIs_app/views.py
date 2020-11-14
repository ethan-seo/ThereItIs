from django.shortcuts import render, redirect
from .models import User, Item, Transaction
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'index.html')
