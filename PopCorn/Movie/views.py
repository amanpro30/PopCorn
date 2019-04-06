<<<<<<< HEAD
from django.shortcuts import render
from Movie.models import Show
from django.db import connection
from Movie.form import ReviewForm, RatingForm
from datetime import date
=======
from Movie.form import ReviewForm
import datetime
from django.db import connection
# from __future__ import unicode_literals
from django.shortcuts import render
from .serializers import *
from rest_framework import generics
>>>>>>> d05c0f9a706a7ad0d6348ab324365a451453859b


# Create your views here.
def hompage(request):
    context = {}
    with connection.cursor() as cur:
        movies_query = "Select * from Movie_Show" \
<<<<<<< HEAD
                       " Where Status = 'R' and type = 'M'"
=======
                       " Where Status = 'R' and type = 'm'"
>>>>>>> d05c0f9a706a7ad0d6348ab324365a451453859b
        cur.execute(movies_query)
        context['theater_movies'] = cur.fetchall()

        tvseries_query = "Select * from Movie_Show " \
<<<<<<< HEAD
                         "Where Status = 'R' And type= 'T' "
        cur.execute(tvseries_query)
        context['rs'] = cur.fetchall()

        movies_query = "Select * from Movie_Show where type= 'M'" \
=======
                         "Where Status = 'R' And type= 'tv' "
        cur.execute(tvseries_query)
        context['rs'] = cur.fetchall()

        movies_query = "Select * from Movie_Show where type= 'm'" \
>>>>>>> d05c0f9a706a7ad0d6348ab324365a451453859b
                       " ORDER BY Avg_rating DESC"
        cur.execute(movies_query)
        context['top_rated'] = cur.fetchall()

        most_reviewed_query = " With count_table(id,no) as " \
                              "(Select m.id,count(*) as no from movie_show m, movie_review r " \
<<<<<<< HEAD
                              "where m.type = 'M' " \
                              "and m.id = r.show_id " \
=======
                              "where m.type = 'm' " \
                              "and m.id = r.movie_id " \
>>>>>>> d05c0f9a706a7ad0d6348ab324365a451453859b
                              "group by m.id " \
                              "order by no desc) " \
                              " Select * from movie_show " \
                              "where movie_show.id in (Select id from count_table) "
        cur.execute(most_reviewed_query)
        context['most_reviewed'] = cur.fetchall()

<<<<<<< HEAD
        movies_query = "Select * from Movie_Show where type= 'T'" \
=======
        movies_query = "Select * from Movie_Show where type= 'tv'" \
>>>>>>> d05c0f9a706a7ad0d6348ab324365a451453859b
                       " ORDER BY Avg_rating DESC"
        cur.execute(movies_query)
        context['tv_top_rated'] = cur.fetchall()

        most_reviewed_query = " With count_table(id,no) as " \
                              "(Select m.id,count(*) as no from movie_show m, movie_review r " \
                              "where m.type = 'tv' " \
<<<<<<< HEAD
                              "and m.id = r.show_id " \
=======
                              "and m.id = r.movie_id " \
>>>>>>> d05c0f9a706a7ad0d6348ab324365a451453859b
                              "group by m.id " \
                              "order by no desc) " \
                              " Select * from movie_show " \
                              "where movie_show.id in (Select id from count_table) "
        cur.execute(most_reviewed_query)
        context['tv_most_reviewed'] = cur.fetchall()
<<<<<<< HEAD
    print(context)
=======

>>>>>>> d05c0f9a706a7ad0d6348ab324365a451453859b
    return render(request, 'html/basehome.html', context)


def movies(request, filter):
    with connection.cursor() as cur:
        data = []
        if filter == 'top_rated':
            movies_query = "Select * from Movie_Show where type= 'm'" \
                           "ORDER BY Avg_rating DESC"
            cur.execute(movies_query)
        elif filter == 'all_alphabet':
            movies_query2 = "Select * from Movie_Show where type= 'm'" \
                            "ORDER BY Movie_title ASC"
            cur.execute(movies_query2)
        elif filter == 'all_release_date':
            movies_query = "Select * from Movie_Show where type= 'm'" \
                           "ORDER BY ReleaseDate DESC"
            cur.execute(movies_query)
        elif filter == 'top_grossers':
            movies_query = "Select * from Movie_Show where type= 'm'" \
                           "ORDER BY Boc DESC"
            cur.execute(movies_query)
        movies_tuple = cur.fetchall()
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
            print(celebrities)
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
        }
        print(context['data'])
        return render(request, 'html/showlist.html', context)


def tvseries(request, filter):
    with connection.cursor() as cur:
        data = []
        if filter == 'top_rated':
            movies_query = "Select * from Movie_Show where type= 'tv'" \
                           " ORDER BY Avg_rating DESC"
            cur.execute(movies_query)
        elif filter == 'all_alphabet':
            movies_query2 = "Select * from Movie_Show where type= 'tv'" \
                            "ORDER BY Movie_title ASC"
            cur.execute(movies_query2)
        elif filter == 'all_release_date':
            movies_query = "Select * from Movie_Show where type= 'tv'" \
                           "ORDER BY ReleaseDate DESC"
            cur.execute(movies_query)
        elif filter == 'top_grossers':
            movies_query = "Select * from Movie_Show where type= 'tv'" \
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
            print(celebrities)
            for j in celebrities:
                if j[9] == 'D':
                    mov1['director'].append(j)
                elif j[9] == 'A':
                    mov1['actors'].append(j)
                elif j[9] == 'P':
                    mov1['producer'].append(j)
                elif j[9] == 'W':
                    mov1['writer'].append(j)
            data.append(mov1)

        context = {
            "count": len(data),
            "data": data,
        }
        print(context['data'])
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
    }
    return render(request, 'html/single_movie.html', context)


def singledetailmovie(request, movie_id):
    with connection.cursor() as cur:
        if request.method == 'POST':
            reviewform = ReviewForm(request.POST)
            ratingform = RatingForm(request.POST)
            if reviewform.is_valid():
<<<<<<< HEAD
                title = reviewform.cleaned_data['Title']
                statement = reviewform.cleaned_data['Statement']
                postquery = "Insert into Movie_Review(show_id,user_id,title,statement,PostDate) " \
                            "values " \
                            " ({},{},'{}','{}','{}')"
                postquery = postquery.format(movie_id, request.user.id, title, statement, date.today())
=======
                title = reviewform.cleaned_data['review_title']
                statement = reviewform.cleaned_data['review_statement']
                postquery = "Insert into Movie_Review(movie_id,user_id,review_title,review_statement, post_date) " \
                            "values " \
                            " ({},{},'{}','{}','{}')"
                postquery = postquery.format(movie_id, request.user.id, title, statement, str(datetime.datetime.now()))
>>>>>>> d05c0f9a706a7ad0d6348ab324365a451453859b
                cur.execute(postquery)
            if ratingform.is_valid():
                if(ratingform.cleaned_data['stars']):
                    starsrcvd = int(ratingform.cleaned_data['stars'])
                    ratingquery = f"Insert into Movie_Rating(show_id, user_id, stars) values ({movie_id},{request.user.id},{starsrcvd})"
                    cur.execute(ratingquery)
        else:
            reviewform = ReviewForm()
            ratingform = RatingForm()

        movies_query = "Select * from Movie_Show where type= 'm' and id ={}"
        movies_query = movies_query.format(movie_id)
        cur.execute(movies_query)
        movies_tuple = cur.fetchall()
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
            if j[9] == 'D':
                mov1['director'].append(j)
            elif j[9] == 'A':
                mov1['actors'].append(j)
            elif j[9] == 'P':
                mov1['producer'].append(j)
            elif j[9] == 'W':
                mov1['writer'].append(j)
        review_query = "Select * " \
                       "from Movie_review as rcv " \
                       "where rcv.show_id = {}"
        review_query = review_query.format(movie_id)
        cur.execute(review_query)
        reviews = cur.fetchall()
<<<<<<< HEAD
        star_ivd_query = f"Select stars from Movie_rating where user_id = {request.user.id} and show_id= {movie_id}"
        cur.execute(star_ivd_query)
        star_result = cur.fetchall()
        star_count = len(star_result)
        if (star_count == 0):
            star_ivd = None
        else:
            star_ivd = star_result[0][0]

        print(star_count)
=======
        stars_query = "Select AVG(rcv.stars) " \
                      "from Movie_ratings rcv " \
                      "where rcv.movie_id = {}"
        stars_query = stars_query.format(movie_id)
        cur.execute(stars_query)
        stars = cur.fetchall()[0]

>>>>>>> d05c0f9a706a7ad0d6348ab324365a451453859b
    context = {
        'reviews': reviews,
        "count": len(data),
        "data": mov1,
        'reviewform': reviewform,
        'ratingform': ratingform,
        'star_count': star_count,
        "star_ivd": star_ivd,
    }
    print(data)
    return render(request, 'html/single_movie.html', context)


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
