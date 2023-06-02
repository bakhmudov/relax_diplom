from rest_framework import serializers
from .models import Movie, MovieSettings, Seat, ShowTime, Ticket


class MovieSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSettings
        fields = ['title', 'value']


class MovieSerializer(serializers.ModelSerializer):
    settings = MovieSettingsSerializer(many=True)

    class Meta:
        model = Movie
        fields = ['id', 'name', 'description',
                  'age', 'image', 'pushkin',
                  'children', 'settings', ]


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ['id', 'movie', 'showtime', 'row', 'number', 'active', 'occupied', 'price', ]


class ShowTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowTime
        fields = ['id', 'time', 'movie', ]


class TicketSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(max_length=255)
    showtime = serializers.CharField(max_length=5)
    row = serializers.IntegerField()
    number = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    name = serializers.CharField(max_length=255)
    email = serializers.EmailField()

    class Meta:
        model = Ticket
        fields = '__all__'
