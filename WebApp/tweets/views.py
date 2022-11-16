#from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .forms import TweetForm
from .models import Tweets

# Create your views here.

class HomePageView(ListView):
    model = Tweets
    template_name = 'home.html'


class CreatePostView(CreateView):
    model = Tweets
    form_class = TweetForm
    template_name = 'tweets.html'
    success_url: reverse_lazy('home')
