from django.shortcuts import render


from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def home(request):
    return render(request, 'core/home.html')

def login(request):
    return render(request,'home/landing_page.html')