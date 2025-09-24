from django.urls import path
from .views import *

urlpatterns=[
    path("",main,name='main'),
    path("signup",Signup,name='signup'),
    path('todo',todo,name='todo'),
    path('user_login',userlogin,name='user_login'),
    path("user_logout",userlogout,name='user_logout'),
    path("update/<str:pk>",update,name='update'),
    path('delete/<str:pk>',delete,name='delete'),
]