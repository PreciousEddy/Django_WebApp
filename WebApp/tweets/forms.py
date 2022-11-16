from django import forms
from .models import Tweets

class TweetForm(forms.ModelForm):


    class Meta:
        model = Tweets
        fields = ['title', 'image']
