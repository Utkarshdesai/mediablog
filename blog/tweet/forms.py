from django import forms
from .models import tweet 

class tweetform(forms.ModelForm):
    class Meta:
        model = tweet 
        fields = ['user' ,'photo' , 'description']