from django import forms


class ReviewForm(forms.Form):
    review_title = forms.CharField(max_length=100)
    review_statement = forms.CharField(max_length=5000)
