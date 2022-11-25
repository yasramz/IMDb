from django.shortcuts import render
from movies.models import Movie


def movie_list(request):
    movies = Movie.objects.all().filter(is_valid=True)[:8]
    context = {
        'movies': movies
    }
    return render(request, 'movies/movie_list.html', context=context)


def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie': movie
    }
    return render(request, 'movies/detail.html', context=context)
