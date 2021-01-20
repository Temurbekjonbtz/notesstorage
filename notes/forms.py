from django import forms
from django.contrib.auth import get_user_model
from item.models  import Note
from accounts.models import User
from django.forms import ModelForm, Textarea, FileInput, TextInput
class LoginForm(forms.Form):
    
    email = forms.CharField(label="Email",
            widget=forms.EmailInput(
                    attrs={
                        "class": "form-control", 
                        "id":"materialLoginFormPassword"
                    }
                    )
            )
    password = forms.CharField(label="Password",
            widget=forms.PasswordInput(
                    attrs={
                        "class": "form-control", 
                        "id":"materialLoginFormPassword"
                    }
                    )
            )


class RegisterForm(forms.ModelForm):
     class Meta:
        model=User
        fields=('full_name','email','password')
     full_name = forms.CharField(label="Username",
            widget=forms.TextInput(
                    attrs={
                        "class": "form-control", 
                        "id":"materialLoginFormPassword"
                    }
                    )
            )
     email = forms.CharField(label="Email",
            widget=forms.EmailInput(
                    attrs={
                        "class": "form-control", 
                        "id":"materialLoginFormPassword"
                    }
                    )
            )       
     password = forms.CharField(label="Password",
            widget=forms.PasswordInput(
                    attrs={
                        "class": "form-control", 
                        "id":"materialLoginFormPassword"
                    }
                    )
            )
     def clean_email(self):
        email1 = self.cleaned_data.get("email")
        if not "gmail.com" in email1:
            raise forms.ValidationError("Email has to be gmail.com")
        elif User.objects.filter(email=email1):
            raise forms.ValidationError("This email  is  already taken")
        return email1

     def clean_username(self):
        
         username1=self.cleaned_data.get("username")
         if len(username1)<5:
             raise forms.ValidationError("Your name should  consist of more  than 5 chars")
         elif User.objects.filter(username=username1):
             raise forms.ValidationError("This username is  already  taken")
         return username1

     def clean_password(self):
         password=self.cleaned_data.get("password")
         if   password.isalnum():
             raise forms.ValidationError("Your password should be  alphanumeric")
         return password
    

class AddForm(forms.ModelForm):
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
     

    


