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


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Search'}))
    CHOICES = (
        ('0', 'ALL'),
        ('1', 'MOVIES'),
        ('2', 'TV SHOWS'),
        ('3', 'CELEBRITIES'),
    )
    select = forms.ChoiceField(widget=forms.Select, choices=CHOICES)
