from django.forms import ModelForm, TextInput, Textarea
from .models import Blog

class BlogForm(ModelForm):

    class Meta:
        model = Blog
        fields = ['title', 'description']
        widgets = {
            'title': TextInput(attrs={'class':'form-control'}),
            'description': Textarea(attrs={'cols': 80, 'rows': 20, 'class':'form-control'}),
        }