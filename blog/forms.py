from django import forms
from django.contrib.auth.models import User
from blog.models import Post, Comment, UserProfile


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'title', 'text']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'text-input'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea post-content'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']

        widgets = {
            'author': forms.TextInput(attrs={'class': 'text-input'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class UserProfileForm(forms.ModelForm):
    profile_picture = forms.ImageField(required=False)
    info = forms.CharField(required=False)
    webiste = forms.URLField(required=False)

    class Meta:
        model = UserProfile
        exclude = ['user', 'number_of_posts']
