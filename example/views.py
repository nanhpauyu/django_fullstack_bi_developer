# example/views.py

from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate
from .login_requred import login_required
from sqlalchemy import create_engine
import pandas as pd
import os

engine = create_engine(
    f'postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/defaultdb?sslmode=require')
table_name = 'my_data'
schema = 'public'


@login_required
def home(request):
    query = "SELECT * FROM public.my_data;"
    df_result = pd.read_sql(query, engine)
    movie_df = df_result[df_result['type'] == 'Movie']
    tv_show_df = df_result[df_result['type'] != 'Movie']
    content = dict()
    # Movie_count vs show_count
    movie_show_count = df_result.groupby(
        'type').size().reset_index(name='count')
    movie_show_count_label = list(movie_show_count['type'])
    movie_show_count_data = list(movie_show_count['count'])
    content['movie_show_count_label'] = movie_show_count_label
    content['movie_show_count_data'] = movie_show_count_data
    # Yearly Movie and Tv show add to Netflix
    movie_groupby_year = movie_df.groupby('year').size()
    yearly_add_label = movie_groupby_year.index.to_list()
    yearly_movie_sum = movie_groupby_year.values
    tv_show_groupby_year = tv_show_df[tv_show_df['year'] != 0].groupby(
        'year').size()
    tv_show_groupby_year = tv_show_groupby_year.reindex(range(tv_show_df[tv_show_df['year'] != 0]['year'].min(
    ), tv_show_df[tv_show_df['year'] != 0]['year'].max() + 1), fill_value=0)
    yearly_tv_show_sum = tv_show_groupby_year.values
    content['yearly_add_label'] = yearly_add_label
    content['yearly_movie_sum'] = yearly_movie_sum
    content['yearly_tv_show_sum'] = yearly_tv_show_sum
    
    # Top Genres
    # genres = df_result['listed_in'].str.split(', ').explode()
    # top_genres = genres.value_counts().head(10)
    # top_genres_label = top_genres.index.to_list()
    # top_genres_data = top_genres.values
    # content['top_genres_label'] = top_genres_label
    # content['top_genres_data'] = top_genres_data
    # return HttpResponse('Hello')
    return render(request, 'overview.html', content)


@login_required
def movies(request):
    query = "SELECT * FROM public.my_data where type='Movie';"
    df_result = pd.read_sql(query, engine)
    return HttpResponse('Movies')


@login_required
def tv_shows(request):
    return HttpResponse('TV Show')


def login(request):
    if 'user' in request.session:
        return redirect('home')
    else:
        if request.method == 'GET':
            return render(request, 'login.html')
        else:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is None:
                content = {'error': True}
                return render(request=request, template_name='login.html', context=content)
            else:
                request.session['user'] = user.username
                return redirect('home')


@login_required
def logout(request):
    try:
        del request.session["user"]
    except KeyError:
        pass
    return redirect('login')
