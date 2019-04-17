from django.shortcuts import render


smartphoneReviews = [

{
	'author': 'Tom Smith',	
	'rating': '5 Stars',	
	'review': 'It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.',	
	'date': '17/04/2019'	
		
},

]

smartwatchReviews = [

{
	'author': 'Tracy Bent',	
	'rating': '3 Stars',	
	'review': 'It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.',	
	'date': '17/04/2019'	
		
},


]


tabletReviews = [

{
	'author': 'Salma Shikdar',	
	'rating': '2 Stars',	
	'review': 'It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.',	
	'date': '17/04/2019'	
		
},



]


def home(request):
	return render (request, 'reviewApp/home.html', {'title': 'Home'})

def about(request):
	return render (request, 'reviewApp/about.html', {'title': 'About Us'})

def contact(request):
	return render (request, 'reviewApp/contact.html', {'title': 'Contact Us'})

def smartphone(request):
	daily_report= {
	'smartphoneReviews': smartphoneReviews
	}
	return render (request, 'reviewApp/smartphone.html', daily_report)

def smartwatch(request):
	daily_report= {
	'smartwatchReviews': smartwatchReviews
	}
	return render (request, 'reviewApp/smartwatch.html', daily_report)

def tablet(request):
	daily_report= {
	'tabletReviews': tabletReviews
	}
	return render (request, 'reviewApp/tablet.html', daily_report)



# Create your views here.
