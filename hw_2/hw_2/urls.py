"""
URL configuration for hw_2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from movie.views import movie_list, movie_detail
from blog.views import article_list, article_detail
from .views import home

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('movies/', movie_list),
    path('movies/<int:id>/', movie_detail),
    path('articles/', article_list),
    path('articles/<int:id>/', article_detail),
]
