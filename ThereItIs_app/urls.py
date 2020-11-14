from django.urls import path
from . import views
from django.conf.urls import url  

urlpatterns = [
    path('', views.index),
    # path('main', views.main),
    # path('user/next', views.next),
    # path('user/dashboard', views.dashboard),
    # path('user/loginpage', views.loginpage),
    # path('user/regpage', views.regpage),
    # path('user/register', views.register),
    # path('user/login', views.login),
    # path('user/logout', views.logout),
    # path('user/edituser/<int:id>', views.edituser),
    # path('user/updateuser/<int:id>', views.updateuser),
    # path('item/edititem/<int:id>', views.edititem),
    # path('item/manage_newsletter', views.manageitem),
    # path('item/add_newsletter', views.additem),
    # path('item/viewitems', views.viewitems),
    # path('item/deleteitem/<int:id>', views.deleteitem),
]