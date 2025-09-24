from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
# Create your views here.
def main(request):
    todos=Todolist.objects.filter(completed=True)
    complete=TodoForm()
    for todo in todos:
        todo.delete()
    list_of_todo=None
    if request.user.is_authenticated:
        userid=request.user.id
        list_of_todo=Todolist.objects.filter(user=userid)
    
    return render(request,"main.html",{'today_works':list_of_todo})

def Signup(request):
    userform=UserForm()
    if request.method=='POST':
        userform=UserForm(request.POST)
        if userform.is_valid():
            userform.save()
            messages.success(request,"you have registered")
            return redirect('main')
        elif request.POST["password1"] != request.POST["password2"]:
            messages.error(request,"password miss match")
        else:
            messages.error(request,"your password must be strong")
            

    return render(request,'signup.html',{"form":userform})
@login_required(login_url='user_login')
def todo(request):
    todofrm=TodoForm()
    if request.method == 'POST':
        todofrm=TodoForm(request.POST)
        if todofrm.is_valid():
            created=todofrm.save(commit=False)
            created.user=request.user
            created.save()
            messages.success(request,"you have successfully submitted ")
            return redirect('main')
        else:
            messages.error(request,"try again later")

    return render(request,"todos.html",{'todoform':todofrm})



def userlogin(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        authenticated=authenticate(request,username=username,password=password)
        if authenticated is not None:
            login(request,authenticated)
            return redirect('main')
        
    return render(request,"login.html")


def userlogout(request):
    logout(request)
    return redirect('user_login')

@login_required(login_url='user_login')
def update(request,pk):
    todo=Todolist.objects.get(id=pk)
    form=TodoForm(instance=todo)
    if request.method=='POST':
        form=TodoForm(request.POST)
        if form.is_valid():
            created=form.save(commit=False)
            created.user=request.user
            created.save()
            messages.success(request,"you have successfully updated")
            return redirect('main')
        else:
            messages.error(request,"try again later")

    return render(request,"update.html",{"form":form,"todo":todo})

@login_required(login_url='user_login')
def delete(request,pk):
    todo=Todolist.objects.get(id=pk)
    todo.delete()
    return redirect('main')
