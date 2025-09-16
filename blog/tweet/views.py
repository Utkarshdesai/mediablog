from django.shortcuts import render
from .models import Tweet
from .forms import tweetform , UserRegisterationForm
from django.shortcuts import get_object_or_404 , redirect
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import login

# Create your views here.
def home(request):
    return render(request , 'tweet.html')

# List down all the tweets 
def List_tweets(request):
    # fetch tweet from model 
    Tweets = Tweet.objects.all().order_by('-created_at')
    # pass to templates 
    return render( request , 'tweet_list.html' , { 'tweets': Tweets } )


# Create the new tweet 
@login_required
def New_tweet(request):
    if request.method == 'POST':
      form = tweetform(request.POST , request.FILES)
      if form.is_valid():
          
          tweet = form.save(commit=False)
          tweet.user = request.user
          tweet.save()
          return redirect('tweet_list')  
    else:
        form = tweetform()

    return render(request , 'New_tweet.html' , {'form' : form})
    
      

# edit twwets
@login_required
def Edit_tweet(request , tweet_id):
    tweets = get_object_or_404(Tweet , pk= tweet_id , user = request.user)
    if request.method == 'POST':
      form = tweetform(request.POST , request.FILES , instance = tweets)
      if form.is_valid():
          tweets = form.save(commit=False)
          tweets.user = request.user
          tweets.save()
          return redirect('tweet_list')        
    else:
        form = tweetform(instance = tweets)

    return render( request , 'New_tweet.html' , {'form' : form})

@login_required
def delete_tweet(request , tweet_id):
    tweets = get_object_or_404(Tweet , pk =tweet_id , user = request.user)
    if request.method == "POST":
        tweets.delete()
        return redirect('tweet_list')
    return render( request , 'tweet_confirm_delete.html' , {'tweet' : tweets})


def Register(request):
    if request.method == 'POST':
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request , user)
            return redirect('tweet_list')     
    else:
        form = UserRegisterationForm()
    return render( request , 'registration/register.html' , {'form' : form })
    
    

    
    


