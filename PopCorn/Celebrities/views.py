from django.shortcuts import render


# Create your views here.
def celeb(request, filter):
    return render(request, 'html/cleblist.html')
