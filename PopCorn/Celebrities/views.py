from django.shortcuts import render
from django.db import connection


# Create your views here.
from Movie.form import SearchForm


def celeb(request, filter):
    with connection.cursor() as cur:
        query_celebrities = "SELECT DISTINCT * " \
                            "FROM Celebrities_celebrity"
        cur.execute(query_celebrities)
        celebrities = cur.fetchall()
        count = len(celebrities)
        context = {
            "count": count,
            "celebs": celebrities,
            'searchform': SearchForm(),
        }
        print(celebrities)
        return render(request, 'html/cleblist.html', context)


def single_celeb(request, celeb_id):
    with connection.cursor() as cur:
        query_celebrities = f"SELECT * " \
                            f"FROM Celebrities_celebrity" \
                            f" WHERE id={celeb_id}"
        cur.execute(query_celebrities)
        celebrities = cur.fetchall()
        query_key = f"SELECT Tag_Name" \
                    f" FROM Celebrities_Tag" \
                    f" WHERE celeb_id={celeb_id}"
        cur.execute(query_key)
        keywords = cur.fetchall()
        context = {
            "celebs": celebrities,
            "keywords": keywords,
            'searchform': SearchForm(),
        }
        print(celebrities)
        return render(request, 'html/celebritysingle.html', context)
