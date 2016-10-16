from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.db.models import F
import operator
import pickle
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


from .forms import SnippetForm, UserForm
from .models import Snippet
from django.db.models import Q

def redirecthome(request):
	return HttpResponseRedirect('/home/snippets/')

def home(request):
	template_name = 'home/home.html'
	snippet_list = Snippet.objects.all()

	key = 'my_qs'

	
	query = request.GET.get("q")
	sort = request.GET.get("s")
	page_request_var = "page"
	page = request.GET.get(page_request_var)

	if query == None and sort == None:
		try:
			snippet_list.query = pickle.loads(request.session[key])
		except: 
			snippet_list = snippet_list.order_by('-timestamp')
	else:
		if query:
			snippet_list = snippet_list.filter(Q(title__contains=query) | Q(tags__contains=query) | Q(author__contains=query))
		if str(sort)  == "Sort by Name":
			snippet_list = snippet_list.order_by('title')
		elif str(sort)  == "Sort by Up Votes":
			snippet_list = snippet_list.order_by('-upvotes')
		elif str(sort)  == "Sort by Down Votes":
			snippet_list = snippet_list.order_by('-downvotes')
		else:
			snippet_list = snippet_list.order_by('-timestamp')
		request.session[key] = pickle.dumps(snippet_list.query)

	paginator = Paginator(snippet_list,5)


	try:
		snippets = paginator.page(page)
	except PageNotAnInteger:
		snippets = paginator.page(1)
	except EmptyPage:
		snippets = paginator.page(paginator.num_pages)
	context = {
		"snippets":snippets,
		'range': range(1,paginator.num_pages+1),
		'page_request_var':page_request_var,
	}

 	return render(request, template_name, context)

def submit(request):
	template_name = 'home/submit.html'
	form = SnippetForm(request.POST or None)
	context={
		"form": form,
	}
	return render(request, template_name, context)

def add_snippet(request):
	template_name = 'home/submit.html'
	form = SnippetForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		if not request.user.username == "":
			instance.author = request.user.username
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form": form,
	}
	return render(request, template_name, context)

def edit_snippet(request, id=None):
	template_name = 'home/submit.html'
	instance = get_object_or_404(Snippet, id=id)
	form = SnippetForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"title": instance.title,
		"instance": instance,
		"form":form,
		"rqust":'/home/snippets/' + id + '/edit_snippet/',
	}
	return render(request, template_name, context)

def upvote_snippet(request, id=None):
	instance = Snippet.objects.get(id=id)
	instance.upvotes = instance.upvotes + 1
	instance.save(update_fields=['upvotes'])
	return HttpResponseRedirect(instance.get_absolute_url())

def downvote_snippet(request, id=None):
	instance = Snippet.objects.get(id=id)
	instance.downvotes = instance.downvotes + 1
	instance.save(update_fields=['downvotes'])
	return HttpResponseRedirect(instance.get_absolute_url())

def delete_snippet(request, id=None):
	instance = get_object_or_404(Snippet, id=id)
	instance.delete()
	messages.success(request, "Deletetion Successful!")
	return HttpResponseRedirect('/home/')


def view_snippet(request, id):
	template_name = 'home/view_snippet.html'
	context = {
		"snippet":Snippet.objects.get(id=id),
		"rqust":'/home/snippets/' + id + '/',
	}

 	return render(request, template_name, context)

def logout_user(request):
	template_name = 'home/login.html'
	logout(request)
	form = UserForm(request.POST or None)
	context = {
		"form": form,
	}
	return render(request, template_name, context)


def login_user(request):
	template_name = 'home/login.html'
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/home/snippets/')
			else:
				return render(request, template_name, {'error_message': 'Your account has been disabled'})
		else:
			return render(request, template_name, {'error_message': 'Invalid login'})
	return render(request, template_name)


def register(request):
	template_name = 'home/register.html'
	form = UserForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user.set_password(password)
		user.save()
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/home/snippets/')
	context = {
	    "form": form,
	}
	return render(request, template_name, context)

