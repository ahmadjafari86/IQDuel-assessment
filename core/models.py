from django.db import models, transaction
from rest_framework.exceptions import ValidationError


class League(models.Model):
    name = models.CharField(max_length=255, unique=True)
    max_players = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=255, unique=True)
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name='players')

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        with transaction.atomic():
            if self.pk is None:
                if self.league and self.league.players.count() >= self.league.max_players:
                    raise ValidationError("Maximum number of players reached for this league.")
            super().save(*args, **kwargs)


class Match(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name='matches')
    player1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='matches_as_player1')
    player2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='matches_as_player2')

    def __str__(self):
        return f"Match in {self.league.name} ({self.player1} vs {self.player2})"