from django.urls import path
from . import views 


urlpatterns = [

path('', views.home, name='reviewApp-home'),

path('about/', views.about, name='reviewApp-about'),

path('contact/', views.contact, name='reviewApp-contact'),

path('smartphone/', views.smartphone, name='reviewApp-smartphone'),

path('smartwatch/', views.smartwatch, name='reviewApp-smartwatch'),

path('tablet/', views.tablet, name='reviewApp-tablet'),


]	