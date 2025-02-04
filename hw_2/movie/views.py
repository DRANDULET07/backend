from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Movie

@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all().values()
    return Response(list(movies))

@api_view(['GET'])
def movie_detail(request, id):
    try:
        movie = Movie.objects.get(id=id)
        return Response({"title": movie.title, "description": movie.description, "producer": movie.producer, "duration": movie.duration})
    except Movie.DoesNotExist:
        return Response({"error": "Movie not found"}, status=404)

