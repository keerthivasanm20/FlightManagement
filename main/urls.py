from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
     
     path('', views.sample),
     path('sample', views.sample),
     path("signup",views.signup),
     path("login",views.Login),
     path("logout",views.logout),
     path("add",views.add),
     path("view",views.view),
     path("book",views.book),
     path("logsample",views.logsample),
     path("del",views.dele),
     path("deleadmin",views.deleadmin),

]
