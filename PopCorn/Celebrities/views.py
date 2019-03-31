from django.shortcuts import render


# Create your views here.
def celeb(request):
    return render(request, 'html/cleblist.html')
