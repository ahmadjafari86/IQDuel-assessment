import json
import random
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from .models import League, Player, Match
from .serializers import LeagueSerializer, PlayerSerializer, MatchSerializer




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

    channel_layer = get_channel_layer()
    matches = Match.objects.filter(league=league)
    serializer = MatchSerializer(matches, many=True)
    async_to_sync(channel_layer.group_send)(
        f"league_{league.id}",
        {"type": "new_match", "message": json.dumps(serializer.data)},
    )

    return Response({"message": "Matchmaking completed."}, status=status.HTTP_200_OK)


class MatchmakingView(APIView):
    def post(self, request, league_id):
        try:
            league = League.objects.get(pk=league_id)
            return perform_matchmaking(league)
        except League.DoesNotExist:
            return Response({"error": "League not found."}, status=status.HTTP_404_NOT_FOUND)


class MatchScoreUpdateView(APIView):
    def post(self, request, **kwargs):
        try:
            league = League.objects.get(pk=kwargs['league_id'])
            match = Match.objects.get(pk=kwargs['match_id'], league=league)
            match.score1 = random.randint(1, 100)
            match.score2 = random.randint(1, 100)
            match.save()

            channel_layer = get_channel_layer()
            serializer = MatchSerializer(match)
            async_to_sync(channel_layer.group_send)(
                f"league_{match.league_id}",
                {"type": "match_update", "message": json.dumps(serializer.data)},
            )
        except League.DoesNotExist:
            return Response({"error": "League not found."}, status=status.HTTP_404_NOT_FOUND)
        except Match.DoesNotExist:
            return Response({"error": "Match not found."}, status=status.HTTP_404_NOT_FOUND)

        return Response({"message": "Match score updated."}, status=status.HTTP_200_OK)
