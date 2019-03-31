from django.shortcuts import render


# Create your views here.
def hompage(request):
    return render(request, 'html/basehome.html')


def movies(request):
    return render(request, 'html/showlist.html')


def tvseries(request):
    return render(request, 'html/showlist.html')


