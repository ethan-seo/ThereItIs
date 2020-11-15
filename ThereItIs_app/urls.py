from django.urls import path
from . import views
from django.conf.urls import url  

urlpatterns = [
    path('', views.index),
    # path('user/next', views.next),
    path('dashboard', views.dashboard),
    path('regpage', views.regpage),
    path('register', views.register),
    path('loginpage', views.loginpage),
    path('login', views.login),
    path('logout', views.logout),
    # path('user/edituser/<int:id>', views.viewuser),
    # path('user/edituser/<int:id>', views.edituser),
    # path('user/updateuser/<int:id>', views.updateuser),
    # path('item/edititem/<int:id>', views.edititem),
    # path('item/manage_newsletter', views.manageitem),
    # path('item/add_newsletter', views.additem),
    # path('item/viewitems', views.viewitems),
    # path('item/deleteitem/<int:id>', views.deleteitem),
    #ADD INVENTORY, ORDERS, & TRANSACTIONS PATHS (SEE NAVBAR ON INDEX.HTML FOR ESTABLISHED PATHS)
]