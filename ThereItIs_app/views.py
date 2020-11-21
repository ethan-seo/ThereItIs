from django.shortcuts import render, redirect
from .forms import AddItemForm
from .models import *
from django.contrib import messages
import bcrypt

# Create your views here.

def index(request):
    return redirect('/user/loginpage')
    
def loginpage(request):
    return render(request, 'loginpage.html')

def regpage(request):
    return render(request, 'regpage.html')

def register(request):
    if request.method == "POST":
        errors = User.objects.create_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/user/regpage')
        else:
            #create an account for our User
            hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            user = User.objects.create(
                first_name=request.POST['first_name'], 
                last_name=request.POST['last_name'], 
                email=request.POST['email'], 
                password=hashed_pw)
            request.session['user_id'] = user.id
            return redirect('/user/dashboard') #the main page of the application
    return redirect(request, '/')

def login(request):
    if request.method == "POST":
        errors = User.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            user = User.objects.filter(email=request.POST['email'])
            if len(user) > 0:
                user = user[0]
                if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                    request.session['user_id'] = user.id
                    return redirect('/user/dashboard')
    return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

def dashboard(request):
    if 'user_id' not in request.session:
        messages.error(request, "You need to register or log in!")
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'all_items': Item.objects.all(),
        'current_page': "dashboard",
    }
    return render(request, 'dashboard.html', context)

def inventory(request):
    if 'user_id' not in request.session:
        messages.error(request, "You need to register or log in!")
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'all_items': Item.objects.all(),
        'current_page': "inventory",
    }
    return render(request, 'main_inventory.html', context)

def edituser(request):
    if 'user_id' not in request.session:
        messages.error(request, "You need to register or log in!")
        return redirect('/')
    context = {
        "user": User.objects.get(id=request.session['user_id']),
        'current_page': "dashboard",
    }
    return render(request, 'editprofile.html', context)

def viewuser(request):
    if 'user_id' not in request.session:
        messages.error(request, "You need to register or log in!")
        return redirect('/')
    context = {
        "user": User.objects.get(id=request.session['user_id']),
        'current_page': "dashboard",
    }
    return render(request, 'editprofile.html', context)

def updateuser(request):
    if request.method == "POST":
        errors = User.objects.update_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/user/edituser/')
        hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        user_to_update = User.objects.get(id=request.session['user_id'])
        user_to_update.first_name = request.POST['first_name']
        user_to_update.last_name = request.POST['last_name']
        user_to_update.email = request.POST['email']
        user_to_update.password = hashed_pw
        user_to_update.save()
    return redirect('/user/edituser')

def edititem(request, id):
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        "item": Item.objects.get(id=id),
        'current_page': "inventory",
    }
    return render(request, 'itemedit.html', context)

def updateitem(request, id):
    if request.method == "POST":
        # errors = Item.objects.create_validator(request.POST)
        # if len(errors) > 0:
        #     for key, value in errors.items():
        #         messages.error(request, value)
        #     return redirect('/item/edititem/'+str(id))
        item_to_update = Item.objects.get(id=id)
        item_to_update.sku = request.POST['sku']
        item_to_update.productname = request.POST['productname']
        item_to_update.productdesc = request.POST['productdesc']
        item_to_update.quanity = request.POST['quanity']
        item_to_update.location = request.POST['location']
        item_to_update.save()
    return redirect('/item/edititem/'+str(id))

def orderpage(request):
    if 'user_id' not in request.session:
        messages.error(request, "You need to register or log in!")
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'all_items': Item.objects.all(),
        'current_page': "order",
    }
    return render(request, 'low_quant.html', context)

def transactionpage(request):
    if 'user_id' not in request.session:
        messages.error(request, "You need to register or log in!")
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'all_items': Item.objects.all(),
        'current_page': "transaction",
    }
    return render(request, 'transactions.html', context)

def deleteitem(request, id):
    if request.method == "POST":
        item_to_delete = Item.objects.get(id=id)
        item_to_delete.delete()
    return redirect('/item/viewitems')

def additem_form(request):
    form = AddItemForm()
    context={
        'form':form
    }
    return render(request,"add_item.html",context)
def additem(request):
    print("add item initiated")
    if request.method == "POST":
        print("form method is post")
        form = AddItemForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            print("Valid Form Saving")
            form.save()
            return redirect('/item/inventory')
        else:
            print("Form is invalid")
        
    return render(request, 'add_item.html',{'form':form})
    
    


def addstock(request, id):
    if request.method == "POST":
        # errors = Item.objects.create_validator(request.POST)
        # if len(errors) > 0:
        #     for key, value in errors.items():
        #         messages.error(request, value)
        #     return redirect('/item/viewitems)
        current_item = Item.objects.get(id=id)
        new_item = Item.objects.create(sku=current_item.sku, productname=current_item.productname, productdesc=current_item.productdesc, quanity=request.POST['quanity'], location=request.POST['location'])
    return redirect('/item/edititem/'+str(id))