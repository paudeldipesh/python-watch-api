from watchlist_app.models import Movie
from django.http import JsonResponse

# Create your views here.
# Movies List View
def movie_list(request):
  movies = Movie.objects.all()
  data = {
    'movies': list(movies.values())
  }
  return JsonResponse(data)

# Movie Detail View
def movie_detail(request, pk):
  movie = Movie.objects.get(pk=pk)
  data = {
    'name': movie.name,
    'description': movie.description,
    'active': movie.active
  }
  return JsonResponse(data)
  