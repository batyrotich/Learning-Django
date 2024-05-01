from django.shortcuts import render
from watchlist_app.models import Movie

# to return a json response
from django.http import JsonResponse

# Create your views here.

def movie_list(request):
    movies = Movie.objects.all()
    data ={
        'movies': list(movies.values())
    }
    
    return JsonResponse(data)


def movie_details(request, pk):
    movie = Movie.objects.get(pk=pk)
    #create a data dictionary with individula objects
    data ={
        'name' : movie.name,
        'description' : movie.description,
        'active': movie.active
    }
 
    return JsonResponse(data)
    
    