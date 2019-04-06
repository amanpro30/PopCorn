from django.shortcuts import render
from django.db import connection

# Create your views here.
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
        context = {
            "celebs": celebrities,
        }
        print(celebrities)
        return render(request, 'html/celebritysingle.html', context)
