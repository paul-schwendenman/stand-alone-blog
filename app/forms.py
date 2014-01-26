from django import forms

class PostForm(forms.Form):
    title = forms.CharField(max_length=60)
    body = forms.CharField(widget=forms.Textarea)
