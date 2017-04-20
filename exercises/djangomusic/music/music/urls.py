from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^history/', include('history.urls')),
    url(r'^admin/', admin.site.urls),
]