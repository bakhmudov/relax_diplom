from django.contrib import admin
from .models import Movie, MovieSettings, ShowTime, Seat, Ticket


class MovieSettingsAdmin(admin.ModelAdmin):
    pass


class MovieAdmin(admin.ModelAdmin):
    pass


class ShowTimeAdmin(admin.ModelAdmin):
    list_display = ['id', 'time', 'movie']


class SeatAdmin(admin.ModelAdmin):
    pass


class TicketAdmin(admin.ModelAdmin):
    pass


admin.site.register(Movie, MovieAdmin)
admin.site.register(MovieSettings, MovieSettingsAdmin)
admin.site.register(ShowTime, ShowTimeAdmin)
admin.site.register(Seat, SeatAdmin)
admin.site.register(Ticket, TicketAdmin)
