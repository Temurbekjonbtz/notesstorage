from django import forms
from django.contrib.auth import get_user_model
from item.models  import Note
from accounts.models import User
from django.forms import ModelForm, Textarea, FileInput, TextInput


class EditForm(forms.ModelForm):
     class Meta:
        model = Note
        fields = ('title','text', 'file1', )

        labels={
            "title":"Title of your note",
            "file1":"Store  your  file if  any",
            "text":"Your note"
        }

        widgets = {
            "title":TextInput(
                attrs={
                "autocomplete":"off",
                 "class": "form-control", 
                "id":"materialLoginFormPassword",
            }
            ),
            "file1":FileInput(
                attrs={
                "class": "form-control", 
                "id":"materialLoginFormPassword"  
                }
            ),
            "text":Textarea(
                attrs={
                "autocomplete":"off",
                 "class": "form-control", 
                "id":"materialLoginFormPassword",
            })
            
        }
     

    