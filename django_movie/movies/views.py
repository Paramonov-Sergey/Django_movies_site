from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from.forms import *
from.models import *
from django.db.models import Q



class Main(View):
    def get(self,request):
        genres=Genre.objects.all()
        films=Movie.objects.all()
        year=request.GET.getlist('year','')
        genre_list=request.GET.getlist('genre_name','')
        year_genre = Movie.objects.filter(Q(genres__in=genre_list) | Q(year__in=year)).distinct()
        search_quary= request.GET.get('search','')
        search_movies = Movie.objects.filter(Q(title__icontains=search_quary) | Q(english_title__icontains=search_quary))

        if year or genre_list:
            return render(request, 'index.html', context={'movies': year_genre, 'genres': genres,'films':films})

        elif  search_quary:
            return  render(request,'index.html',context={'movies':search_movies,'genres':genres,'films':films})
        else:
            return render(request,'index.html',context={'movies':films,'genres':genres,'films':films})




class FilmDetail(View):
    def get(self,request,id):
        film=Movie.objects.prefetch_related('actors').get(id=id)
        genres=Genre.objects.all()
        rating_stars=RatingStar.objects.all()
        return render(request,'movies/film_detail.html',context={'film':film,'rating_stars':rating_stars,'genres':genres})

    def post(self,request,id):
        form=ReviewsForm(request.POST)
        film = Movie.objects.get(id=id)
        genres = Genre.objects.all()
        if form.is_valid():
            form=form.save(commit=False)
            form.movie_id=id
            form.save()
            return redirect(film)
        return render(request,'movies/film_detail.html',context={'film':film,'form':form,'genres':genres})


class RaitingDetail(View):
    def post(self,request,id):
        rating_form=RatingForm(request.POST)
        if rating_form.is_valid():
            rating_form=rating_form.save(commit=False)
            movie_id=id




class GenreDetail(View):
    def get(self,request,url):
        genre_object=Genre.objects.get(url__iexact=url)
        movies=genre_object.film_genres.all()
        genres=Genre.objects.all()
        films=Movie.objects.all()
        return render(request,'movies/genre_detail.html',context={'genre_object':genre_object,'genres':genres,'films':films,'movies':movies})


class ActorDetail(View):
    def get(self,request,id):
        actor=Actor.objects.get(id=id)
        genres=Genre.objects.all()
        return render(request,'movies/actor_detail.html',context={'actor':actor,'genres':genres})