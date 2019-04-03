from django.shortcuts import render


# Create your views here.
def rating(request):
    return render(request, 'html/showlist.html')


def activity(request):
    return render(request, 'html/basehome.html')


def favorites(request):
    return render(request, 'html/showlist.html')


def watchlist(request):
    return render(request, 'html/showlist.html')


def profile(request):
    return render(request, 'html/profile.html')
