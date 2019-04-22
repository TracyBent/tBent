from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  
from django.urls import reverse



class SmartphoneReviews(models.Model):

	rating=models.CharField(max_length=50)
	review=models.TextField()
	date=models.DateTimeField(default=timezone.now)
	author=models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.rating

	def get_absolute_url(self):
		return reverse('smartphoneReviews-detail', kwargs={'pk': self.pk})


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


class Product(models.Model):

	Product_Name=models.CharField(max_length=50)
	Manufacturer=models.CharField(max_length=50)
	Average_Cost =models.CharField(max_length=5)
	Category=models.CharField(max_length=50)
	Release_Date=models.DateField(default=timezone.now)
	Description=models.TextField()
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	def __str__(self):
		return self.Product_Name


class NewsArticle(models.Model):

	Header=models.CharField(max_length=100)
	Description=models.TextField()
	Date_Posted=models.DateTimeField(default=timezone.now)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	def __str__(self):
		return self.Header





# Create your models here.
