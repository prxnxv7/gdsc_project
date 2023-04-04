from .models import UploadImage
from django import forms
  
class UserImage(forms.ModelForm):  
    class Meta:  
        # To specify the model to be used to create form  
        model = UploadImage  
        # It includes all the fields of model  
        fields = ['name','phone','image','comment'] 

        widgets ={
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'phone' : forms.TextInput(attrs={'class' : 'form-control'}),
            'comment' : forms.Textarea(attrs={'class' : 'form-control'}),
        }