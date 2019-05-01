# from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
# from .forms import NewUserForm
# # Create your views here.
#
# def registration(request):
#     if request.method == 'POST':
#         form = NewUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = NewUserForm()
#     return render(request, 'registration/registration.html', {'form': form})

from django.contrib.sites.shortcuts import get_current_site
from django.db import connection
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string

from Movie.form import SearchForm
from .forms import SignUpForm, ProfileForm, UpdateProfile, UserForm
from .tokens import account_activation_token
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.core.mail import send_mail
from django.db import connection
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import pairwise_distances
from Movie.models import Show, Rating


def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if form.is_valid() and profile_form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            usr_profile = profile_form.save(commit=False)
            usr_profile.user = user
            usr_profile.save()
            send_mail(
                'hello from project python',
                'email is working here',
                'popcornproject123@gmail.com',
                [user.email],
                fail_silently=False,
            )
            login_user = authenticate(username=form.cleaned_data['username'],
                                      password=form.cleaned_data['password1'], )
            login(request, login_user)
            print(user.email)
            return redirect('Movie:home')
    else:
        form = SignUpForm()
        profile_form = ProfileForm()
    return render(request, 'registration/registration.html', {'form': form, 'profile': profile_form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('landing')
    else:
        return render(request, 'registration/account_activation_invalid.html')


def email_verification(request):
    return render(request, 'registration/email_verification.html')


from django.shortcuts import render


def recommend(request):
    print('recommend')
    with connection.cursor() as cur:
        movies_query = "Select user_id,age,region,first_name from registration_profile"
        cur.execute(movies_query)
        profiles = cur.fetchall()
        print(profiles)
        user_id = []
        age = []
        region = []
        sex = []
        for i in profiles:
            user_id.append(i[0])
            age.append(i[1])
            region.append(i[2])
            sex.append(i[3])
        profiles = {'user_id': user_id, 'age': age, 'region': region, 'sex': sex}
        users = pd.DataFrame(profiles)
        ratings_query = "Select User_id, Show_id, Stars from movie_rating"
        cur.execute(ratings_query)
        ratings = cur.fetchall()
        print(ratings)
        user_id = []
        show_id = []
        stars = []
        for i in ratings:
            user_id.append(i[0])
            show_id.append(i[1])
            stars.append(i[2])
        ratings = {'user_id': user_id, 'item_id': show_id, 'stars': stars}
        ratings = pd.DataFrame(ratings)
        n_users = ratings.user_id.unique().shape[0]
        n_items = ratings.item_id.unique().shape[0]
        data_matrix = np.zeros((n_users + 2, n_items + 1))
        print(ratings)
        for line in ratings.itertuples():
            data_matrix[line[1], line[2]] = line[3]
        user_similarity = 1 - pairwise_distances(data_matrix, metric='cosine')

        def predict(ratings, similarity):
            mean_user_rating = ratings.mean(axis=1)
            ratings_diff = (ratings - mean_user_rating[:, np.newaxis])
            pred = mean_user_rating[:, np.newaxis] + similarity.dot(ratings_diff) / np.array(
                [np.abs(similarity).sum(axis=1)]).T
            return pred

        user_prediction = predict(data_matrix, user_similarity)
        print(user_prediction)
    user_recommend_data = []
    for i in user_prediction[request.user.id]:
        user_recommend_data.append(i)
    user_recommend_data = user_recommend_data[1:]
    movie_rated = Rating.objects.filter(User_id=request.user.id)
    movie_rated_list = []
    for i in movie_rated:
        print(i.Show_id)
        movie_rated_list.append(i.Show_id)
    print('movie Rated')
    print(movie_rated)

    user_recommend_data_sorted = sorted(user_recommend_data, reverse=True)
    print(user_recommend_data_sorted)
    movie_id = []
    for i in range(len(user_recommend_data_sorted)):
        for j in range(len(user_recommend_data)):
            if user_recommend_data_sorted[i] == user_recommend_data[j]:
                movie_id.append(j+1)
    movie_id_common = []
    for i in movie_rated:
        for j in movie_id:
            print(i.Show_id,j)
            if i.Show_id == j:
                movie_id_common.append(j)
    movie_id_common = movie_id_common[0:10]
    print('miu', movie_id_common,'mid',movie_id)
    for i in movie_id_common:
        movie_id.remove(i)
    movie_recommended_list = []
    for i in movie_id:
        # with connection.cursor() as cur:
            # movies_query = " Select * from movie_show where id ={} "
            # movies_query = movies_query.format(id)
            # cur.execute(movies_query)
            # movies = cur.fetchall()
        movies = Show.objects.filter(id=i)
        movie_recommended_list.append(movies)
    context = {
        "profiles": users,
        "recommended_movies": movie_recommended_list,
    }
    return render(request, 'registration/recommend.html', context)


# Create your views here.
def rating(request):
    ratingquery = "Select * from "
    return render(request, 'html/showlist.html')


def activity(request):
    return render(request, 'html/basehome.html')


def favorites(request):
    context = {
        'token': 'favorites',
        'image': request.user.profile.profile_picture,
        'searchform': SearchForm(),
    }
    with connection.cursor() as cur:
        query = "Select * from movie_show " \
                " where id in " \
                " (Select Show_id from movie_favourite where Type='F' " \
                "And User_id = {})"
        query = query.format(request.user.id)
        cur.execute(query)
        context['data'] = cur.fetchall()
        print(context['data'])
    return render(request, 'html/watchfavlist.html', context)


def watchlist(request):
    context = {
        'token': 'watchlist',
        'image': request.user.profile.profile_picture,
        'searchform': SearchForm(),
    }
    with connection.cursor() as cur:
        query = "Select * from movie_show " \
                " where id in " \
                " (Select Show_id from movie_favourite where Type='W' " \
                "And User_id = {})"
        query = query.format(request.user.id)
        cur.execute(query)
        context['data'] = cur.fetchall()
    return render(request, 'html/watchfavlist.html', context)

#
# def rated(request):
#     context = {
#         'token': 'rated',
#         'searchform': SearchForm(),
#     }
#     with connection.cursor() as cur:
#         query = "Select  movie_show.Title,movie_show.ReleaseDate,movie_show.Duration,movie_show.Description,movie_show.Image,movie_show.Avg_rating,movie_show.Num_rating,movie_rating.Stars from movie_show right join movie_rating on movie_show.show" \
#                 " where movie_show.id in " \
#                 " (Select Show_id from movie_rating where User_id = {})"
#         print(request.user.id)
#         query = query.format(request.user.id)
#         cur.execute(query)
#         context['data'] = cur.fetchall()
#         print(context['data'])
#     return render(request, 'html/rated.html', context)





def rated(request):
    context = {
        'token': 'rated',
        'searchform': SearchForm(),
    }
    with connection.cursor() as cur:
        query = "Select  movie_show.Title,movie_show.ReleaseDate,movie_show.Duration,movie_show.Description,movie_show.Image,movie_show.Avg_rating,movie_show.Num_rating,movie_rating.Stars from movie_show,movie_rating" \
                " where movie_show.id=movie_rating.Show_id and User_id = {}"
        print(request.user.id)
        query = query.format(request.user.id)
        cur.execute(query)
        context['data'] = cur.fetchall()
        print(context['data'])
    return render(request, 'html/rated.html', context)







def profile(request):
    if request.method == 'POST':
        profileupdateform = UpdateProfile(request.POST, instance=request.user.profile)
        userform = UserForm(data=request.POST, instance=request.user)
        if profileupdateform.is_valid() and userform.is_valid():
            profileupdateform.save()
            userform.save()
    else:
        profileupdateform = UpdateProfile(instance=request.user.profile)
        userform = UserForm(instance=request.user)
    context = {
        'token': 'profile',
        'image': request.user.profile.profile_picture,
        'searchform': SearchForm(),
        'profileupdateform': profileupdateform,
        'userform': userform,
    }
    print('image', context['image'])
    return render(request, 'html/profile.html', context)


def changepassword(request):
    context = {
        'token': 'Change your password',
        'image': request.user.profile.profile_picture,
        'searchform': SearchForm(),
    }
    return render(request, 'html/changepassword.html', context)
