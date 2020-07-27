from django.conf import settings
from django.db import models

class Headline(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()
	url = models.TextField(default='')

	def __str__(self):
		return self.title