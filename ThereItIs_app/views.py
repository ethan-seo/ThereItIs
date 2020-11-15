from django.shortcuts import render, redirect
from .models import User, Item, Transaction
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'loginpage.html')

#LOGIN/REGISTRATION ACTIONS

def register(request):
    if request.method == "POST":
        print(request.POST)
        errors = User.objects.create_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            new_user = User.objects.create(firstname=request.POST['firstname'], lastname=request.POST['lastname'], email=request.POST['email'], password=hashed_pw, ship_address=request.POST['ship_address'], ship_city=request.POST['ship_city'], ship_state=request.POST['ship_state'], ship_zip=request.POST['ship_zip'], bill_address=request.POST['bill_address'], bill_city=request.POST['bill_city'], bill_state=request.POST['bill_state'], bill_zip=request.POST['bill_zip'], card_num=request.POST['card_num'], card_sec=request.POST['card_sec'], card_exp=request.POST['card_exp'])
            request.session['user'] = new_user.id
            return redirect('/dashboard')
    return redirect('/')

def login(request):
    if request.method == "POST":
        logged_user = User.objects.filter(email=request.POST['email'])
        if len(logged_user) > 0:
            logged_user = logged_user[0]
            print(request.POST['password'].encode())
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['user'] = logged_user.id
                return redirect('/dashboard')
        messages.error(request, 'Email or password is incorrect')
    return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

#LOGIN/REGISTRATION PAGES

def loginpage(request):
    return redirect('/')

def regpage(request):
    return redirect('/')

#MAIN DASHBOARD PAGE

def dashboard(request):
    # if 'user' not in request.session:
    #     return redirect('/')
    # loggedinuser = User.objects.get(id= request.session['user'])
    context = {
        "all_items": Item.objects.all(),
        #'user': loggedinuser
    }
    return render(request, "dashboard.html", context)

#MAIN INVENTORY PAGE


#ONE ITEM INVENTORY PAGE


#LOW QUANTITY ITEMS PAGE


#TRANSACTIONS PAGE