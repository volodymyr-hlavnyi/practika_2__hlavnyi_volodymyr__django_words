from django.contrib import admin

from apps.words.models import Room, GameWord


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name_of_room', 'created_at')


@admin.register(GameWord)
class GameWordAdmin(admin.ModelAdmin):
    list_display = ('name_of_gamer', 'word', 'room', 'created_at')
