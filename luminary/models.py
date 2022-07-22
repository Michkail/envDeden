from django.shortcuts import models


class User(models.Model):
	paragraph = models.TextField(blank=True, null=False)
	
