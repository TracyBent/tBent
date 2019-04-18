from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 



class SmartphoneReviews(models.Model):

	rating=models.CharField(max_length=50)
	review=models.TextField()
	date=models.DateTimeField(default=timezone.now)
	author=models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.rating


class SmartwatchReviews(models.Model):

	rating=models.CharField(max_length=50)
	review=models.TextField()
	date=models.DateTimeField(default=timezone.now)
	author=models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.rating



class TabletReviews(models.Model):

	rating=models.CharField(max_length=50)
	review=models.TextField()
	date=models.DateTimeField(default=timezone.now)
	author=models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.rating

# Create your models here.
