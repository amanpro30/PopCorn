from django import forms
from django.forms import ModelForm
from Movie.models import Rating, Review


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['Title', 'Statement']


class RatingForm(ModelForm):
    stars = forms.IntegerField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Rating
        fields = ['stars']
