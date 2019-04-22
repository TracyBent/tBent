from django.urls import path
from . import views 
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, PostListView1


urlpatterns = [

path('', views.home, name='reviewApp-home'),

path('about/', views.about, name='reviewApp-about'),

path('contact/', views.contact, name='reviewApp-contact'),

path('smartphone/', PostListView.as_view(), name='reviewApp-smartphone'),

path('smartphoneReviews/<int:pk>', PostDetailView.as_view(), name='smartphoneReviews-detail'),

path('smartphoneReviews/new/', PostCreateView.as_view(), name='smartphoneReviews-create'),

path('smartphoneReviews/<int:pk>/update/', PostUpdateView.as_view(),name='smartphoneReviews-update'),

path('smartphoneReviews/<int:pk>/delete/', PostDeleteView.as_view(),name='smartphoneReviews-delete'),

path('user/<str:username>', UserPostListView.as_view(), name='user-smartphoneReviews'),




path('smartwatch/', PostListView1.as_view(), name='reviewApp-smartwatch'),

path('tablet/', views.tablet, name='reviewApp-tablet'),


]	