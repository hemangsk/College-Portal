from django.conf.urls import url
from student import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register', views.register, name='register'),
    url(r'^login', views.user_login, name='login'),
    url(r'^attendance', views.attendance, name='attendance'),
    url(r'^logout', views.user_logout, name='logout'),
    url(r'^student', views.user_login, name='student'),
]
