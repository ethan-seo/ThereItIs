from django.urls import path
from . import views
from django.conf.urls import url  

urlpatterns = [
    path('', views.index),
    path('user/loginpage', views.loginpage),
    path('user/regpage', views.regpage),
    path('user/login', views.login),
    path('user/register', views.register),
    path('user/dashboard', views.dashboard),
    path('user/logout', views.logout),
    path('item/inventory', views.inventory),
    path('user/edituser', views.edituser),
    path('user/updateuser', views.updateuser),
    path('item/edititem/<int:id>', views.edititem),
    path('item/updateitem/<int:id>', views.updateitem),
    path('item/orderpage', views.orderpage),
    path('item/transactionpage', views.transactionpage),
    path('item/deleteitem/<int:id>', views.deleteitem),
    path('item/additem', views.additem),
    path('item/additem_form', views.additem_form),
    path('item/addstock/<int:id>', views.addstock),
]