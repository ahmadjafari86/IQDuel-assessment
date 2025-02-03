from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import League, Player, Match
from .serializers import LeagueSerializer, PlayerSerializer, MatchSerializer
import random



class LeagueListCreateView(generics.ListCreateAPIView):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer

class LeagueDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer

class PlayerCreateView(generics.CreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class MatchListView(generics.ListAPIView):
    serializer_class = MatchSerializer

    def get_queryset(self):
        league_id = self.kwargs['league_id']
        return Match.objects.filter(league_id=league_id)



def perform_matchmaking(league):
    players = list(league.players.all())
    random.shuffle(players)

    Match.objects.filter(league=league).delete()

    for i in range(0, len(players) -1 , 2):
        Match.objects.create(league=league, player1=players[i], player2=players[i+1])

    return Response({"message": "Matchmaking completed."}, status=status.HTTP_200_OK)


class MatchmakingView(APIView):
    def post(self, request, league_id):
        try:
            league = League.objects.get(pk=league_id)
            return perform_matchmaking(league)
        except League.DoesNotExist:
            return Response({"error": "League not found."}, status=status.HTTP_404_NOT_FOUND)
