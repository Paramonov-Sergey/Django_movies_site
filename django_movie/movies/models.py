from django.db import models
from datetime import date
from django.shortcuts import reverse




class Category(models.Model):
    name=models.CharField(max_length=150,verbose_name='Категория')
    description=models.TextField(verbose_name='Описание')
    url=models.SlugField(max_length=160,unique=True,verbose_name='Слаг')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'


class Actor(models.Model):
    name=models.CharField(max_length=100,verbose_name='Имя')
    english_name=models.CharField(max_length=100,verbose_name='Имя на английском',null=True)
    age=models.DateField(default=date.today,verbose_name='Возраст')
    description=models.TextField(verbose_name='Описание')
    image=models.ImageField(upload_to='actors/',verbose_name='Изображение')
    height=models.DecimalField(max_digits=3,decimal_places=2,verbose_name='Рост',null=True)
    devorced=models.ManyToManyField('self',related_name='devorced_related',verbose_name='Развод',blank=True)
    married=models.OneToOneField('self',on_delete=models.SET_NULL,related_name='wife_or_husband',verbose_name='Брак',null=True,blank=True)
    native_country=models.CharField(max_length=100 ,verbose_name='Место рождения',null=True)
    genres=models.ManyToManyField('Genre',verbose_name='Жанры',related_name='film_genre',blank=True)
    gender=models.ForeignKey('Gender',on_delete=models.CASCADE,verbose_name='Пол')
    sum_movies = models.PositiveSmallIntegerField(verbose_name='Количество фильмов',default=0,null=True)


    def get_absolute_url(self):
        return reverse('actor_detail_url',kwargs={'id':self.id})


    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Человек'
        verbose_name_plural='Люди'



class Genre(models.Model):
    name=models.CharField(max_length=100,verbose_name='Имя')
    description=models.TextField(verbose_name='Описание')
    url=models.SlugField(max_length=100,unique=True,verbose_name='Слаг')

    def get_absolute_url(self):
        return reverse('genre_detail_url',kwargs={'url':self.url})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Жанр'
        verbose_name_plural='Жанры'


class Movie(models.Model):
    title=models.CharField(max_length=100,verbose_name='Название')
    english_title=models.CharField(max_length=100,verbose_name='Название на английском',null=True)
    tagline=models.CharField(max_length=100,default=' ',verbose_name='Слоган')
    description=models.TextField(verbose_name='Описание')
    description_2 = models.TextField(verbose_name='Подробное описание',null=True)
    poster=models.ImageField(upload_to='movies/',verbose_name='Постер')
    year=models.PositiveSmallIntegerField(default=2019,verbose_name='Дата выхода')
    country=models.CharField(max_length=30,verbose_name='Страна')
    directors=models.ManyToManyField(Actor,verbose_name='Режисер',related_name='film_director')
    actors=models.ManyToManyField(Actor,verbose_name='Актеры',related_name='film_actor')
    genres=models.ManyToManyField(Genre,verbose_name='Жанры',related_name='film_genres')
    world_premiere=models.DateField(default=date.today,verbose_name='Примьера в мире')
    russian_premiere = models.DateField(default=date.today, verbose_name='Примьера в России')
    budget=models.PositiveIntegerField(default=0,help_text='указывать сумму в долларах',verbose_name='Бюджет')
    fees_in_usa= models.PositiveIntegerField( default=0, help_text='указывать сумму в долларах',verbose_name='Сборы в США')
    fees_in_world = models.PositiveIntegerField( default=0, help_text='указывать сумму в долларах',verbose_name='Сборы в мире')
    category=models.ForeignKey(Category,verbose_name='Категория',on_delete=models.SET_NULL,null=True)
    url=models.SlugField(max_length=130,unique=True,verbose_name='Слаг')
    draft=models.BooleanField(default=False,verbose_name='Черновик')
    age=models.PositiveSmallIntegerField(default=0,verbose_name='Возраст')
    scenarists = models.ManyToManyField(Actor, verbose_name='Сценарий', related_name='film_scenarist')
    compositors=models.ManyToManyField(Actor,verbose_name='Композитор',related_name='film_compositor')
    hudogniks=models.ManyToManyField(Actor,verbose_name='Художник',related_name='film_hudognik')
    operators=models.ManyToManyField(Actor,verbose_name='Оператор',related_name='film_operators')
    producer = models.ManyToManyField(Actor, verbose_name='Продюсер', related_name='film_producers')
    treiler=models.FileField(upload_to='treilers/',verbose_name='Трейлер',null=True)
    quality_videos=models.ForeignKey('QualityVideos',on_delete=models.SET_NULL,null=True,verbose_name='Качество видео')


    def get_absolute_url(self):
        return reverse('film_detail_url',kwargs={'id':self.id})


    def __str__(self):
        return self.title



    class Meta:
        verbose_name='Фильм'
        verbose_name_plural='Фильмы'


class MovieShots(models.Model):
    title=models.CharField(max_length=100,verbose_name='Заголовок')
    description=models.TextField(verbose_name='Описание')
    image=models.ImageField(upload_to='movie_shots/',verbose_name='Фото')
    movie=models.ForeignKey(Movie,related_name='movieshots',verbose_name='Фильм',on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Кадр из фильма'
        verbose_name_plural='Кадры из фильма'


class RatingStar(models.Model):
    value=models.PositiveSmallIntegerField(default=0,verbose_name='Значение')

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name='Звезда рейтинга'
        verbose_name_plural='Звезды рейтинга'
        ordering=['-value']

class Rating(models.Model):
    ip=models.CharField(max_length=15,verbose_name='IP адрес')
    star=models.ForeignKey(RatingStar,on_delete=models.CASCADE,verbose_name='звезда')
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE,verbose_name='фильм')

    def str(self):
        return f'{self.star} - {self.movie}'

    class Meta:
        verbose_name='Рейтинг'
        verbose_name_plural='Рейтинги'


class Reviews(models.Model):
    email=models.EmailField(verbose_name='Email')
    name=models.CharField(max_length=100,verbose_name='Имя')
    text=models.TextField(max_length=5000,verbose_name='Ваш комментарий')
    parent=models.ForeignKey('self',verbose_name='Родитель',on_delete=models.SET_NULL,blank=True,null=True)
    movie=models.ForeignKey(Movie,verbose_name='Фильм',on_delete=models.CASCADE,related_name='review_movie')

    def __str__(self):
        return f'{self.name} - {self.movie}'

    class Meta:
        verbose_name='Отзыв'
        verbose_name_plural='Отзывы'


class Gender(models.Model):
    title=models.CharField(max_length=20,verbose_name='Пол')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Пол'
        verbose_name_plural = 'Пол'


class QualityVideos(models.Model):
    title=models.CharField(max_length=20,verbose_name='Наименование качества')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Качество видео'
        verbose_name_plural = 'Качество видео'


