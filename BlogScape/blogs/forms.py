from django import forms
from .models import blog, comments

class blogform (forms.ModelForm):
    class Meta :
        model = blog
        fields = {'title', 'content'}

class commentForm(forms.ModelForm):
    class Meta :
        model = comments
        fields = {'Add_Comment'}
        widgets = {
            'content': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Write a comment...'})
        }

class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)
