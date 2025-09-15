from django.shortcuts import render
from .models import tweet
from .forms import tweetform
from django.shortcuts import get_object_or_404 , redirect

# Create your views here.
def home(request):
    return render(request , 'tweet.html')

# List down all the tweets 
def List_tweets(request):
    # fetch tweet from model 
    Tweets = tweet.objects.all().order_by('-created_at')
    # pass to templates 
    return render( request , 'tweet_list.html' , { 'tweet': Tweets } )


# Create the new tweet 
def New_tweet(request):
    if request.method == 'POST':
      form = tweetform(request.POST , request.FILES)
      if form.is_valid():
          
          tweet = form.save(commit=False)
          tweet.user = request.user
          tweet.save()
          return redirect('List_tweets')  
    else:
        form = tweetform()

    return render( request , 'New_tweet.html' , {'form' : form})
    
    

     
    # empty form to user 

    # render form in templates 
def Edit_tweet(request , tweet_id):
    tweet = get_object_or_404(tweet ,pk= tweet_id , user = request.user)
    if request.method == 'POST':
      form = tweetform(request.POST , request.FILES , instance=tweet)
      if form.is_valid():
          tweet = form.save(commit=False)
          tweet.user = request.user
          tweet.save()
          return redirect('List_tweets')
          
      
      pass
    else:
        form = tweetform(instance = tweet)

    return render( request , 'New_tweet.html' , {'form' : form})

def delete_tweet(request , tweet_id):
    tweet = get_object_or_404(tweet ,pk= tweet_id , user = request.user)
    if request.method == "POST":
        tweet.delete()
        return redirect('List_tweets')
    return render( request , 'tweet_confirm_delete.html' , {'tweet' : tweet})
    
    

    
    


