from django.urls import path
from . import views






urlpatterns = [
   
    path('' , views.List_tweets , name="tweet_list"),
    path('newtweet/' , views.New_tweet , name='new_tweet'),
    path('<int:tweet_id>/edit/', views.Edit_tweet , name="new_tweet"),
    path('<int:tweet_id>/delete/', views.delete_tweet , name="delete_tweet"),
    path(' register/', views.Register , name="register"),
    
    path('<int:tweet_id>/delete/', views.delete_tweet , name="delete_tweet"),
] 
