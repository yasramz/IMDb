from django.shortcuts import render
from movies.models import Movie


def movie_list(request):
    movies = Movie.objects.all().filter(is_valid=True)[:8]
    context = {
        'movies': movies
    }
    return render(request, 'movies/movies_list.html', context=context)
