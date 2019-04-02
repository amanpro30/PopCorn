from django.shortcuts import render
from Movie.models import Show
from django.db import connection

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
                              "FROM Movie_Show AS M, Movie_ShowCelebrity AS MS WHERE M.id=MS.id" \
                              " ORDER BY Avg_rating DESC"
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
        query_a = "SELECT * FROM Movie_Show AS m, Movie_ShowCelebrity AS ms, Celebrities_celebrities AS c WHERE m.id=ms.Show_id and c.id=ms.Celebrity_id ORDER BY Avg_rating DESC"
        cur.execute(query_a)
        a = cur.fetchall()
        print(a)

        return render(request, 'html/showlist.html', context)




def tvseries(request,filter):
    return render(request, 'html/showlist.html')


