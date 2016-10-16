from django import forms
from django.contrib.auth.models import User
from .models import Snippet

class SnippetForm(forms.ModelForm):
	class Meta:
		model = Snippet
		fields = ['title','tags','content']

		def clean_title(self):
			title = self.cleaned_data.get('title')
			return title

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
