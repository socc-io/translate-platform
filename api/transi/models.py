from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Document(models.Model):
	owner = models.ForeignKey(User)
	title = models.CharField(max_length=200)
	created_date = models.DateTimeField(default=timezone.now)
	original_lang = models.CharField(max_length=10)
	target_lang = models.CharField(max_length=10)

	def __str__(self):
		return self.title

class Paragraph(models.Model):
	document = models.ForeignKey(Document)
	content = models.TextField()

	def __str__(self):
		return self.content

class Translated(models.Model):
	paragraph = models.ForeignKey(Paragraph)
	content = models.TextField()

	def __str__(self):
		return self.content
