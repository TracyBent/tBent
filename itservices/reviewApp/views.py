from django.shortcuts import render


def home(request):
	return render (request, 'reviewApp/home.html')

def about(request):
	return render (request, 'reviewApp/about.html')

def contact(request):
	return render (request, 'reviewApp/contact.html')

# Create your views here.
