from django.contrib.auth.models import User
from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    age = models.CharField(max_length=3)
    image = models.ImageField(upload_to='static/')
    pushkin = models.BooleanField(default=False)
    children = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ShowTime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='show_time')
    time = models.CharField(max_length=5)

    def __str__(self):
        return f'{self.time} - {self.movie}'


class MovieSettings(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='settings')
    title = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title} - Фильм: {self.movie}'


class Seat(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, default=None)
    showtime = models.ForeignKey(ShowTime, on_delete=models.CASCADE, related_name='seats')
    row = models.PositiveIntegerField()
    number = models.PositiveIntegerField()
    active = models.BooleanField(default=False)
    occupied = models.BooleanField(default=False)
    price = models.FloatField()

    class Meta:
        unique_together = ('movie', 'showtime', 'row', 'number')

    def __str__(self):
        return f'Фильм: {self.movie} || Ряд: {self.row}, Место №: {self.number}'


class Ticket(models.Model):
    movie_title = models.ForeignKey(Movie, on_delete=models.CASCADE, blank=True, null=True)
    showtime = models.ForeignKey(ShowTime, on_delete=models.CASCADE, blank=True, null=True)
    # seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    row = models.PositiveIntegerField(blank=True, null=True)
    number = models.PositiveIntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f'Ticket #{self.pk}'
