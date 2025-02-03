from django.contrib import admin
from .models import League, Player, Match

@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'max_players')
    search_fields = ('name',)

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'league')
    search_fields = ('name',)
    list_filter = ('league',)

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('id', 'league', 'player1', 'player2')
    list_filter = ('league',)