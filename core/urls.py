from django.urls import path
from . import views

urlpatterns = [
    path('leagues/', views.LeagueListCreateView.as_view(), name='league-list-create'),
    path('leagues/<int:pk>/', views.LeagueDetailView.as_view(), name='league-detail'),
    path('players/', views.PlayerCreateView.as_view(), name='player-create'),
    path('leagues/<int:league_id>/matches/', views.MatchListView.as_view(), name='match-list'),
    path('leagues/<int:league_id>/matchmaking/', views.MatchmakingView.as_view(), name='matchmaking'),
]