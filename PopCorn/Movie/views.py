from django.shortcuts import render
from Movie.models import *
from Celebrities.models import *
from django.db import connection
#from __future__ import unicode_literals
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
from Movie import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
def hompage(request):
    return render(request, 'html/basehome.html')


def movies(request, filter):
    with connection.cursor() as cur:
        query_count_movies = "SELECT COUNT(*) " \
                             "FROM Movie_Show " \
                             "WHERE type='m'"
        cur.execute(query_count_movies)
        count = cur.fetchall()
        context = {
            "count": count,
        }
        if filter == 'top_rated':
            query_top_rated = "SELECT * " \
                              "FROM Movie_Show " \
                              "ORDER BY Avg_rating DESC"
            cur.execute(query_top_rated)
            top_rated = cur.fetchall()
            context['top_rated']=top_rated
        elif filter == 'all_name':
            query_sort_name = "SELECT * " \
                            "FROM Movie_Show " \
                            "ORDER BY Movie_title ASC"
            cur.execute(query_sort_name)
            sort_name = cur.fetchall()
            context['sort_name']=sort_name
        elif filter == 'all_release_date':
            query_sort_release_date = "SELECT * " \
                                "FROM Movie_Show " \
                                "ORDER BY ReleaseDate DESC"
            cur.execute(query_sort_release_date)
            sort_release_date = cur.fetchall()
            context['sort_release_date']=sort_release_date
        elif filter == 'top_grossers':
            query_top_grossers ="SELECT * " \
                           "FROM Movie_Show " \
                           "ORDER BY Boc DESC"
            cur.execute(query_top_grossers)
            top_grossers = cur.fetchall()
            context['top_grossers']=top_grossers
        return render(request, 'html/showlist.html', context)



class ShowListView(generics.ListCreateAPIView):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer

class ShowView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ShowSerializer
    queryset = Show.objects.all()

class AwardsListView(generics.ListCreateAPIView):
    queryset = Awards.objects.all()
    serializer_class = AwardsSerializer


class AwardsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AwardsSerializer
    queryset = Awards.objects.all()


class CelebritiesListView(generics.ListCreateAPIView):
    queryset = Celebrities.objects.all()
    serializer_class = CelebritiesSerializer

class CelebritiesView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CelebritiesSerializer
    queryset = Celebrities.objects.all()


def tvseries(request,filter):
    return render(request, 'html/showlist.html')


