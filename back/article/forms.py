from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=50)
    content = forms.CharField()

class Comment(forms.Form):
    content = forms.CharField()