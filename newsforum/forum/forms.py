from django import forms
from forum.models import Post, Category, Comment


class PostCreateForm(forms.Form):
    title = forms.CharField(max_length=255, widget=forms.TextInput(attrs={"class":"form-control"}))
    content = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control", 'rows': 5}))
    category = forms.ModelChoiceField(empty_label=None, queryset=Category.objects.all(), widget=forms.Select(attrs={"class":"form-control"}))


class CommentCreateForm(forms.Form):

    content = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", 'rows': 5}))

