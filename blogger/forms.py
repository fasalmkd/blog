from django import forms
from . models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields='__all__'
        labels ={
            'title':'Enter title',
            'content':'Write a content',
            'image':'upload image',
        }