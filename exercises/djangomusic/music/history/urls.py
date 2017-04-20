from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^artists/', views.artists, name='artists'),
    url(r'^artistdetails/', views.artist_details, name='artist_details'),
    url(r'^$', views.index, name='index'),
]