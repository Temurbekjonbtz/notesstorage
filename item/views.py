from django.shortcuts import render, redirect
from .models import Note
from .forms import  EditForm
from django.http import HttpResponse, HttpResponseRedirect, StreamingHttpResponse,Http404
import os
from django.conf import settings
import uuid
import shutil
from django.http import JsonResponse
import  json
from django.core import serializers
# Create your views here.
def stream_http_download(request, file_path):
    try:
        response = StreamingHttpResponse(open(settings.MEDIA_ROOT+"/"+file_path, 'rb'))
        response['content_type'] = "application/octet-stream"
        response['Content-Disposition'] = 'attachment; filename='+os.path.basename(file_path)[36:len(os.path.basename(file_path))]
        return response
    except Exception:
        raise Http404

def delete_page(request, id):
   if(Note.objects.get_by_id(id=id).file1):
      os.remove(settings.MEDIA_ROOT+"/"+str(Note.objects.get_by_id(id).file1.name))
   Note.objects.filter(id=id).delete()
   return redirect("/home/")


def hello(request):
   

   return HttpResponse("<h1> Hello </h1>")

def search_page(request):
   if request.method == "GET" and request.is_ajax():
       
        term=request.GET['info']
       # Note.objects.all().filter(owner=request.user)
        queryset1 = Note.objects.all().filter(title__icontains=term,owner=request.user)
        queryset2 = Note.objects.all().filter(text__icontains=term,owner=request.user)
       # notes=list(notes)
       
        listOfResults=[]
        for item in list(queryset1) :
             x={
                'link':'/item/'+str(item.pk)+'/',
                'title':item.title
             }
             listOfResults.append(x)
        for item in list(queryset2) :
             x={
                'link':'/item/'+str(item.pk)+'/',
                'title':item.text
             }
             listOfResults.append(x)
   return JsonResponse(listOfResults,safe=False)
   


def item_page(request, id):
   print("Hello")
   instance = Note.objects.get_by_id(id)
   navbar="navbar.html"
   context={
           'navbar':navbar,
           "note":instance,
        }
   return render(request,"item/note.html",context)



def edit_page(request, id):
   instance = Note.objects.get_by_id(id)
   form=EditForm(request.POST or None, request.FILES or None)
   form.fields['title'].initial = instance.title
   form.fields['text'].initial = instance.text
   navbar="navbar.html"
   context={
           'navbar':navbar,
           "note":instance,
           "form":form,
        }
   
   if  form.is_valid():
      print(instance.file1.name)
      title=form.instance.title
      text=form.instance.text
      file1=form.instance.file1.name
      if file1!="":
         if instance.file1.name!="":
           os.remove(settings.MEDIA_ROOT+"/"+str(instance.file1.name))
         file1=str(uuid.uuid4())+file1
         with open(settings.MEDIA_ROOT+"/files/"+file1, 'wb+') as destination:  
               for chunk in form.instance.file1.chunks():  
                   destination.write(chunk)  
         Note.objects.filter(id=instance.id).update(title=title,text=text,file1="files/"+file1)
      else:
         Note.objects.filter(id=instance.id).update(title=title,text=text)
      return redirect("/home/")

   return render(request,"item/edit.html",context)
