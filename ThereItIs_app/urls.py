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
    path('user/viewuser', views.viewuser),
    path('user/edituser', views.edituser),
    path('user/updateuser', views.updateuser),
    path('item/edit/<int:id>', views.edit_item),
    path('item/orderpage', views.orderpage),
    path('item/transactionpage', views.transactionpage),
    path('item/deleteitem/<int:id>', views.deleteitem),
    path('item/add', views.add_item),
    path('item/viewitem/<int:id>', views.viewitem),
    # path('item/additem_form', views.additem_form),
    path('item/addstock/<int:id>', views.addstock),
    path('item/addstockpage/<int:id>', views.addstockpage),
    path('item/orderpagefilter',views.orderpagefilter),
    path('item/expiring', views.expiring)
]