from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm
from django.shortcuts import get_object_or_404 , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseForbidden
from django.contrib.auth import logout
from django.shortcuts import redirect

# Create your views here.
@login_required
def index(request):
    return render(request,'index.html')

@login_required
def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html', {'tweets': tweets})


@login_required(login_url='/accounts/login/')
def tweet_create(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm()
    
    return render(request, 'tweet_form.html', {'form': form})


@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
    return render(request, 'tweet_form.html', {'form': form})


@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)

    if request.user != tweet.user:
        return HttpResponseForbidden(" You are not allowed to delete this tweet.")

    tweet.delete()
    return redirect('tweet_list')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})


@login_required
def my_tweets(request):
    tweets = Tweet.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'my_tweets.html', {'tweets': tweets})

def logout_user(request):
    logout(request)
    return redirect('login')