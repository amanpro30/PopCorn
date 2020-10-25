from django.shortcuts import render
from Movie.models import *
from django.db import connection
from Movie.form import *
import datetime
from datetime import date
import math
from django.contrib.auth.models import User
from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .serializers import *
from rest_framework import generics, filters, fields


def hompage(request):
    context = {}
    with connection.cursor() as cur:
        movies_query = "Select * from movie_show" \
                       " Where Status = 'R' or Status = 'U' and type = 'M' LIMIT 15"
        cur.execute(movies_query)
        context['theater_movies'] = cur.fetchall()

        tvseries_query = "Select * from movie_show " \
                         "Where Status = 'R' And type= 'T' LIMIT 15"
        cur.execute(tvseries_query)
        context['rs'] = cur.fetchall()

        movies_query = "Select * from movie_show where type= 'M'" \
                       " ORDER BY Avg_rating DESC LIMIT 15"
        cur.execute(movies_query)
        context['top_rated'] = cur.fetchall()

        most_reviewed_query = " With count_table(id,no) as " \
                              "(Select m.id,count(*) as no from movie_show m, movie_review r " \
                              "where m.type = 'M' " \
                              "and m.id = r.Show_id " \
                              "group by m.id) " \
                              " Select * from movie_show, count_table " \
                              "where movie_show.id = count_table.id " \
                              " order by no desc "
        cur.execute(most_reviewed_query)
        context['most_reviewed'] = cur.fetchall()

        movies_query = "Select * from movie_show where type= 'T'" \
                       " ORDER BY Avg_rating DESC"
        cur.execute(movies_query)
        context['tv_top_rated'] = cur.fetchall()

        most_reviewed_query = " With count_table(id,no) as " \
                              "(Select m.id,count(*) as no from movie_show m, movie_review r " \
                              "where m.type = 'T' " \
                              "and m.id = r.Show_id " \
                              "group by m.id " \
                              "order by no desc) " \
                              " Select * from movie_show, count_table " \
                              "where movie_show.id = count_table.id " \
                              " order by no desc "
        cur.execute(most_reviewed_query)
        context['tv_most_reviewed'] = cur.fetchall()
    visits_grouped = Visits.objects.filter(
        time__range=[datetime.datetime.now() - datetime.timedelta(days=7), datetime.datetime.now()]).values(
        'Show').annotate(dcount=Count('Show')).order_by('-dcount')
    show_trending = visits_grouped[0]['Show']
    trending_show = Show.objects.filter(id=show_trending)
    context['searchform'] = SearchForm()
    context['trending_show'] = trending_show
    return render(request, 'html/basehome.html', context)


def movies(request, filter, page):
    with connection.cursor() as cur:
        data = []
        page = str((int(page) - 1) * 10)
        if filter == 'top_rated':
            movies_query = f"Select * from movie_show where type= 'm'" \
                           f"ORDER BY Avg_rating DESC LIMIT 10 OFFSET {page}"
            cur.execute(movies_query)
        elif filter == 'all_alphabet':
            movies_query2 = f"Select * from Movie_Show where type= 'm'" \
                            f"ORDER BY Title ASC LIMIT 10 OFFSET {page}"
            cur.execute(movies_query2)
        elif filter == 'all_release_date':
            movies_query = f"Select * from Movie_Show where type= 'm'" \
                           f"ORDER BY ReleaseDate DESC LIMIT 10 OFFSET {page}"
            cur.execute(movies_query)
        elif filter == 'top_grossers':
            movies_query = f"Select * from Movie_Show where type= 'm'" \
                           f"ORDER BY Boc DESC LIMIT 10 OFFSET {page}"
            cur.execute(movies_query)
        movies_tuple = cur.fetchall()
        all_movies_query = "Select count(*) from Movie_Show"
        cur.execute(all_movies_query)
        all_mov = cur.fetchall()
        count_page = math.ceil(all_mov[0][0] / 10)
        for i in movies_tuple:
            query = "SELECT *" \
                    " FROM Movie_ShowCelebrity as msc, Celebrities_Celebrity as mc" \
                    " WHERE msc.Celebrity_id = mc.id " \
                    "AND msc.Show_id={}"
            query = query.format(i[0])
            cur.execute(query)
            celebrities = cur.fetchall()
            mov1 = {
                'movie': i,
                'director': [],
                'producer': [],
                'writer': [],
                'actors': [],
            }
            for j in celebrities:
                if j[1] == 'D':
                    mov1['director'].append(j)
                elif j[1] == 'A':
                    mov1['actors'].append(j)
                elif j[1] == 'P':
                    mov1['producer'].append(j)
                elif j[1] == 'W':
                    mov1['writer'].append(j)
            data.append(mov1)
        context = {
            "count": len(data),
            "data": data,
            "count_page": count_page,
            "count_page_range": range(1, count_page + 1),
            "filter": filter,
            'searchform': SearchForm(),
        }
        return render(request, 'html/showlist.html', context)


def tvseries(request, filter):
    with connection.cursor() as cur:
        data = []
        if filter == 'top_rated':
            movies_query = "Select * from Movie_Show where type= 'T'" \
                           " ORDER BY Avg_rating DESC"
            cur.execute(movies_query)
        elif filter == 'all_alphabet':
            movies_query2 = "Select * from Movie_Show where type= 'T'" \
                            "ORDER BY Movie_title ASC"
            cur.execute(movies_query2)
        elif filter == 'all_release_date':
            movies_query = "Select * from Movie_Show where type= 'T'" \
                           "ORDER BY ReleaseDate DESC"
            cur.execute(movies_query)
        elif filter == 'top_grossers':
            movies_query = "Select * from Movie_Show where type= 'T'" \
                           "ORDER BY Boc DESC"
            cur.execute(movies_query)

        movies_tuple = cur.fetchall()
        for i in movies_tuple:
            query = "SELECT *" \
                    " FROM Movie_ShowCelebrity as msc, Celebrities_Celebrity as mclb" \
                    " WHERE msc.Celebrity_id = mclb.id " \
                    "AND msc.Show_id={}"
            query = query.format(i[0])
            cur.execute(query)
            celebrities = cur.fetchall()
            mov1 = {
                'movie': i,
                'director': [],
                'producer': [],
                'writer': [],
                'actors': [],
            }
            for j in celebrities:
                if j[1] == 'D':
                    mov1['director'].append(j)
                elif j[1] == 'A':
                    mov1['actors'].append(j)
                elif j[1] == 'P':
                    mov1['producer'].append(j)
                elif j[1] == 'W':
                    mov1['writer'].append(j)
            data.append(mov1)

        context = {
            "count": len(data),
            "data": data,
            'searchform': SearchForm(),
        }
    return render(request, 'html/showlist.html', context)
    stars_query = "Select AVG(rcv.stars) " \
                  "from Movie_ratings rcv " \
                  "where rcv.movie_id = {}"
    stars_query = stars_query.format(movie_id)
    cur.execute(stars_query)
    stars = cur.fetchall()[0]
    context = {
        'reviews': reviews,
        "count": len(data),
        "data": mov1,
        'stars': stars,
        'reviewform': reviewform,
        'searchform': SearchForm()
    }
    return render(request, 'html/single_movie.html', context)


def singledetailmovie(request, movie_id):
    with connection.cursor() as cur:
        if request.method == 'POST':
            reviewform = ReviewForm(request.POST)
            ratingform = RatingForm(request.POST)
            if reviewform.is_valid():
                title = reviewform.cleaned_data['Title']
                statement = reviewform.cleaned_data['Statement']
                postquery = "Insert into Movie_Review(show_id,user_id,title,statement,PostDate) " \
                            "values " \
                            " ({},{},'{}','{}','{}')"
                postquery = postquery.format(
                    movie_id, request.user.id, title, statement, date.today())
                cur.execute(postquery)
            if ratingform.is_valid():
                if (ratingform.cleaned_data['stars']):
                    starsrcvd = int(ratingform.cleaned_data['stars'])
                    ratingquery = "Insert into Movie_Rating(show_id, user_id, stars) values ({},{},{})"
                    ratingquery = ratingquery.format(
                        movie_id, request.user.id, starsrcvd)
                    cur.execute(ratingquery)
            user_instance = User.objects.get(id=request.user.id)
            show_instnace = Show.objects.get(id=movie_id)
            if request.body == b'addw':
                Favourite.objects.create(
                    User=user_instance, Type='W', Show=show_instnace)
            elif request.body == b'addf':
                Favourite.objects.create(
                    User=user_instance, Type='F', Show=show_instnace)
            elif request.body == b'delw':
                Favourite.objects.filter(
                    User=request.user.id, Show=movie_id, Type='W').delete()
            elif request.body == b'delf':
                Favourite.objects.filter(
                    User=request.user.id, Show=movie_id, Type='F').delete()
        else:
            reviewform = ReviewForm()
            ratingform = RatingForm()

        movies_query = "Select * from Movie_Show"
        movies_query = movies_query.format(movie_id)
        cur.execute(movies_query)
        movies_tuple = cur.fetchall()
        print(movies_tuple)
        i = movies_tuple[0]
        data = []
        query = "SELECT *" \
                " FROM Movie_ShowCelebrity as msc, Celebrities_Celebrity as mclb" \
                " WHERE msc.Celebrity_id = mclb.id " \
                "AND msc.Show_id={}"
        query = query.format(i[0])
        cur.execute(query)
        celebrities = cur.fetchall()
        mov1 = {
            'movie': i,
            'director': [],
            'producer': [],
            'writer': [],
            'actors': [],
        }
        for j in celebrities:
            if j[1] == 'D':
                mov1['director'].append(j)
            elif j[1] == 'A':
                mov1['actors'].append(j)
            elif j[1] == 'P':
                mov1['producer'].append(j)
            elif j[1] == 'W':
                mov1['writer'].append(j)
        review_query = "Select * " \
                       "from Movie_review as rcv " \
                       "where rcv.show_id = {}"
        review_query = review_query.format(movie_id)
        cur.execute(review_query)
        reviews = cur.fetchall()
        star_ivd_query = f"Select stars from Movie_rating where user_id = {request.user.id} and show_id= {movie_id}"
        cur.execute(star_ivd_query)
        star_result = cur.fetchall()
        star_count = len(star_result)
        if (star_count == 0):
            star_ivd = None
        else:
            star_ivd = star_result[0][0]
    try:
        queryset_fav = Favourite.objects.filter(
            User=request.user.id, Show=movie_id, Type='F')
    except Favourite.DoesNotExist:
        queryset_fav = None
    if queryset_fav is not None:
        fav_count = len(queryset_fav)
    try:
        queryset_watch = Favourite.objects.filter(
            User=request.user.id, Show=movie_id, Type='W')
    except Favourite.DoesNotExist:
        queryset_watch = None
    if queryset_watch is not None:
        watch_count = len(queryset_watch)
    context = {
        'reviews': reviews,
        "count": len(data),
        "data": mov1,
        'reviewform': reviewform,
        'ratingform': ratingform,
        'star_count': star_count,
        "star_ivd": star_ivd,
        'searchform': SearchForm(),
        'fav': fav_count,
        'watchlist': watch_count,
    }
    with connection.cursor() as cur:
        user_instance = User.objects.get(id=request.user.id)
        movie_instance = Show.objects.get(id=movie_id)
        Visits.objects.create(User=user_instance, Show=movie_instance)
    return render(request, 'html/single_movie.html', context)


def searchbox(request):
    context = {}
    with connection.cursor() as cur:
        if request.method == 'POST':
            searchform = SearchForm(request.POST)
            if searchform.is_valid():
                query = searchform.cleaned_data['search']
                select = searchform.cleaned_data['select']
                if select == '0':
                    searchquery = "Select * from movie_show " \
                                  " where MATCH(Title) " \
                                  " AGAINST('{}' IN NATURAL LANGUAGE MODE)"
                    searchquery = searchquery.format(query)
                    cur.execute(searchquery)
                    context['shows'] = cur.fetchall()
                    searchquery = "Select * from celebrities_celebrity " \
                                  " where MATCH(Name) " \
                                  " AGAINST('{}' IN NATURAL LANGUAGE MODE)"
                    searchquery = searchquery.format(query)
                    cur.execute(searchquery)
                    context['celeb'] = cur.fetchall()
                elif select == '1':
                    searchquery = "Select * from movie_show " \
                                  " where MATCH(Title) " \
                                  " AGAINST('{}' IN NATURAL LANGUAGE MODE) " \
                                  "AND Type = 'M' "
                    searchquery = searchquery.format(query)
                    cur.execute(searchquery)
                    context['shows'] = cur.fetchall()
                elif select == '2':
                    searchquery = "Select * from movie_show " \
                                  " where MATCH(Title) " \
                                  " AGAINST('{}' IN NATURAL LANGUAGE MODE) " \
                                  "AND Type = 'T' "
                    searchquery = searchquery.format(query)
                    cur.execute(searchquery)
                    context['shows'] = cur.fetchall()
                elif select == '3':
                    searchquery = "Select * from celebrities_celebrity " \
                                  " where MATCH(Name) " \
                                  " AGAINST('{}' IN NATURAL LANGUAGE MODE)"
                    searchquery = searchquery.format(query)
                    cur.execute(searchquery)
                    context['celeb'] = cur.fetchall()
            context['searchform'] = SearchForm(request.POST)
        else:
            context['searchform'] = SearchForm()
    return render(request, 'html/searchresults.html', context)


def favmod(request, mov_id):
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class ShowListView(generics.ListCreateAPIView):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer


class ShowView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ShowSerializer
    queryset = Show.objects.all()


class CelebrityListView(generics.ListCreateAPIView):
    queryset = Celebrity.objects.all()
    serializer_class = CelebritySerializer


class CelebrityView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CelebritySerializer
    queryset = Celebrity.objects.all()


class AwardListView(generics.ListCreateAPIView):
    queryset = Award.objects.all()
    serializer_class = AwardSerializer


class AwardView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AwardSerializer
    queryset = Award.objects.all()
