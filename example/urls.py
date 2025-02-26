# example/urls.py
from django.urls import path

from example.views import home, login, logout, tv_shows, movies


urlpatterns = [
    path('', home, name='home'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('tv_shows',tv_shows,name='tv_shows'),
    path('movies',movies,name='movies'),
]
