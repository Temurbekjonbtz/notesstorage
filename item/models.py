from django.db import models
from django.contrib.auth import authenticate, get_user_model
from django.utils import timezone
from django.conf import settings
import os, uuid

# Create your models here.


   

  
class NoteManager(models.Manager):
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id) # Product.objects == self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None

    
   

class Note(models.Model):
    owner            = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=None)
    title           = models.CharField(max_length=100)
    text             =models.TextField()
    file1            = models.FileField(blank=True,  upload_to="files")
    timestamp   =   models.DateTimeField(default=timezone.now)
    objects =NoteManager()

    def __str__(self):
        return self.title

    def css_class(self):
        name, extension = os.path.splitext(self.file1.name)
        if extension == '.pdf':
            return 'pdf.jpg'
        elif extension == '.docx':
            return 'doc.jpg'
        elif extension=='':
            return 'empty.jpg'
        else:
            return 'etc.jpg'


    