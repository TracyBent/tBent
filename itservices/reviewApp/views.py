from django.shortcuts import render, get_object_or_404
from .models import SmartphoneReviews 
from .models import SmartwatchReviews 
from .models import TabletReviews 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User


# SmartphoneReviews = [

# {
# 	'author': 'Tom Smith',	
# 	'rating': '5 Stars',	
# 	'review': 'It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.',	
# 	'date': '17/04/2019'	
		
# },

# ]


def home(request):
	return render (request, 'reviewApp/home.html', {'title': 'Home'})

def about(request):
	return render (request, 'reviewApp/about.html', {'title': 'About Us'})

def contact(request):
	return render (request, 'reviewApp/contact.html', {'title': 'Contact Us'})

def smartphone(request):
	daily_report= {
	'smartphoneReviews': SmartphoneReviews.objects.all()
	}
	return render (request, 'reviewApp/smartphone.html', daily_report)

class PostListView(ListView):
	model = SmartphoneReviews
	template_name = 'reviewApp/smartphone.html'
	context_object_name = 'smartphoneReviews'
	ordering = ['-date']
	paginate_by = 5

class UserPostListView(ListView):	

	model = SmartphoneReviews
	template_name = 'reviewApp/user_smartphoneReviews.html'
	context_object_name = 'smartphoneReviews'
	paginate_by = 5

	def get_queryset(self):

		user=get_object_or_404(User,
		username=self.kwargs.get('username'))
		return SmartphoneReviews.objects.filter(author=user).order_by('-date')


class PostDetailView(DetailView):
	model = SmartphoneReviews


class PostCreateView(LoginRequiredMixin, CreateView):
	model = SmartphoneReviews
	fields = ['rating', 'review']

	def form_valid(self, form):

		form.instance.author = self.request.user
		return super() .form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

	model = SmartphoneReviews
	fields = ['rating', 'review']


	def test_func(self):
		smartphoneReviews = self.get_object()
		if self.request.user == smartphoneReviews.author:
			return True
		return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

	model = SmartphoneReviews
	success_url = '/smartphone'

	def test_func(self):
		smartphoneReviews = self.get_object()
		if self.request.user == smartphoneReviews.author:
			return True
		return False


def smartwatch(request):
	daily_report= {
	'smartwatchReviews': SmartwatchReviews.objects.all()
	}
	return render (request, 'reviewApp/smartwatch.html', daily_report)


def tablet(request):
	daily_report= {
	'tabletReviews': TabletReviews.objects.all()
	}
	return render (request, 'reviewApp/tablet.html', daily_report)






# Create your views here.
