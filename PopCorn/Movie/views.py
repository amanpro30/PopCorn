from django.shortcuts import render
from Movie.models import Show
from django.db import connection
from Movie.form import ReviewForm
from datetime import date


# Create your views here.
def hompage(request):
    return render(request, 'html/basehome.html')


def movies(request, filter):
    with connection.cursor() as cur:
        data = []
        if filter == 'top_rated':
            movies_query = "Select * from Movie_Show where type= 'm'" \
                           " ORDER BY Avg_rating DESC"
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
                    " FROM Movie_ShowCelebrity as msc, Celebrities_Celebrities as mc" \
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
                    " FROM Movie_ShowCelebrity as msc, Celebrities_Celebrities as mclb" \
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


def singledetail(request, movie_id):
    with connection.cursor() as cur:
        if request.method == 'POST':
            reviewform = ReviewForm(request.POST)
            if reviewform.is_valid():
                title = reviewform.cleaned_data['review_title']
                statement = reviewform.cleaned_data['review_statement']
                postquery = "Insert into Movie_Review(movie_id,user_id,review_title,review_statement,post_date) " \
                            "values " \
                            " ({},{},'{}','{}','{}')"
                print(date.today())
                postquery = postquery.format(movie_id, request.user.id, title, statement, date.today())
                cur.execute(postquery)

        else:
            reviewform = ReviewForm()

        movies_query = "Select * from Movie_Show where type= 'm' and id ={}"
        movies_query = movies_query.format(movie_id)
        cur.execute(movies_query)
        movies_tuple = cur.fetchall()
        print(movies_tuple[0])
        i = movies_tuple[0]
        data = []
        query = "SELECT *" \
                " FROM Movie_ShowCelebrity as msc, Celebrities_Celebrities as mclb" \
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
                       "from Movie_review rcv " \
                       "where rcv.movie_id = {}"
        review_query = review_query.format(movie_id)
        cur.execute(review_query)
        reviews = cur.fetchall()

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
