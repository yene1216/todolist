from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class Userdesplay(UserAdmin):
    list_display=['username','first_name','last_name','email','password']
admin.site.unregister(User)
admin.site.register(User,Userdesplay)
class DesplayTodo(admin.ModelAdmin):
    list_display=['title','description','created_at','completed','user']
admin.site.register(Todolist,DesplayTodo)
