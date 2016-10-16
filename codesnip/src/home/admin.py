from django.contrib import admin

# Register your models here.
from .forms import SnippetForm, UserForm
from .models import Snippet

class SnippetAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "timestamp", "updated","upvotes","downvotes"]
	form = SnippetForm
	#class Meta:
	#	model = Snippet

admin.site.register(Snippet, SnippetAdmin)
