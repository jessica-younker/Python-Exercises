from django.conf.urls import url
# period below indicates 'same directory (views'

from . import views
# r'^$ is directing to base route url, views.index is module.method, third arg is a name/label for route

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
#^= beginning of string, $= end
