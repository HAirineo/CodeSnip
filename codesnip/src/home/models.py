from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

from django.contrib.auth.models import Permission, User
# Create your models here.

class Snippet(models.Model):
	title = models.CharField(max_length = 100, blank=False, null=False)
	author = models.CharField(default = 'Guest', max_length = 20, blank=False, null=False)
	tags = models.CharField(max_length = 100, blank=True, null=True)
	upvotes = models.IntegerField(default = 0)
	downvotes = models.IntegerField(default = 0)
	content = models.TextField(blank=False, null=False)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)
	updated = models.DateTimeField(auto_now_add = False, auto_now=True)

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('view_snippet', kwargs={"id": self.id})