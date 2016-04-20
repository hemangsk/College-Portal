from django.conf.urls import include, url
from analysis import views
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^display', views.display, name = 'display'),
]