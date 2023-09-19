from django.urls import path
from . import views


urlpatterns = [
    path('', views.news, name="news"),
    path('blogs', views.blogs, name="blogs"),
]
