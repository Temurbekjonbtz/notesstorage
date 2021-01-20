from django.shortcuts import  render ,redirect
from django.contrib.auth import authenticate,   login, logout,get_user_model
from django.http import HttpResponse, HttpResponseRedirect
from  item.models import Note
from .forms import  LoginForm, RegisterForm, AddForm
import  uuid, os
def home_page(request):
        notes=Note.objects.all().filter(owner=request.user)
        notes=list(notes)
        print(notes)
        navbar="navbar.html"
        context={
           'navbar':navbar,
           'notes' :notes,
        }
        return render(request,'home.html',context)
  
def logout_page(request):
        logout(request)
        navbar="empty.html"
        context={
           'navbar':navbar
        }
        return redirect("/login/")

def add(request):
        form=AddForm(request.POST or None, request.FILES or None)
        navbar="navbar.html"
        context={
           'navbar':navbar,
           'form' :form,
           
        }
        
        if form.is_valid() and  request.user.is_authenticated:
           form.instance.owner=request.user
           if form.instance.file1.name!="":
              form.instance.file1.name=str(uuid.uuid4())+form.instance.file1.name
           form.save()
           return HttpResponseRedirect(request.path)
        return render(request,'add.html',context)
   



def register_page(request):
     account=get_user_model()
     form = RegisterForm(request.POST or None)

     context = {
         "navbar":"empty.html",
        "form": form,
     }
     if form.is_valid():
        email=form.cleaned_data["email"]
        password=form.cleaned_data["password"]
        full_name=form.cleaned_data["full_name"]
        account.objects.create_user(email=email,password=password,full_name=full_name)
        return redirect("/login/")
     else:
        return render(request,'register.html',context)


def login_page(request):
     form = LoginForm(request.POST or None)
     if form.is_valid():
        email1  = form.cleaned_data.get("email")
        password1  = form.cleaned_data.get("password")
        print(email1)
        print(password1)

        user = authenticate(request, email=email1,password=password1)
        print(user)
        if user  is  not None:
           login(request,user)
           return redirect("/home/")
        else:
           return HttpResponseRedirect(request.path)
     else:
        context = {
             "navbar":"empty.html",
             "form": form,
        }
        return render(request,'login.html',context )