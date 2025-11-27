from django.contrib import admin
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from .views import tweet_list


from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.tweet_list, name='tweet_list'),
    path('index/', views.index, name='index'),
    path('create/',views.tweet_create,name = 'tweet_create'),
    path('<int:tweet_id>/edit/',views.tweet_edit,name = 'tweet_edit'),
    path('<int:tweet_id>/delete/',views.tweet_delete,name = 'tweet_delete'),
    path('register/', views.register, name='register'),
    path("my-tweets/", views.my_tweets, name="my_tweets"),
    path('', login_required(tweet_list), name='tweet_list'),


] 
