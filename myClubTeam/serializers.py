from rest_framework import serializers
from .models import Team, Player, Match, Standing,playermatchscore


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ["id", "team","name", "position", "number",]
        

class TeamSerializer(serializers.ModelSerializer):
    players = PlayerSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ["id", "name", "coach", "founded_year", "players"]


class TopScorerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = ["name","Allgoals"]

class StandingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Standing
        fields="__all__"




class playermatchscoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = playermatchscore
        fields = ["player","goal_in_match"]

class MatchSerializer(serializers.ModelSerializer):
     
    goals = playermatchscoreSerializer(many=True)

    class Meta:
        model = Match
        fields = ["id","home_team","away_team","home_score","away_score","goals"]

 
    def create(self, validated_data):
        
         print(validated_data)
         score_names = validated_data.pop("goals")
         print(validated_data)
         match = Match.objects.create(**validated_data)
         print(score_names)
         for name in score_names:
             player_name = name["player"]
             player = Player.objects.get(name=player_name)

             playermatchscore.objects.create(
                 match=match,
                 player=player,
                 goal_in_match=name["goal_in_match"],
                 
                 
                )
        
             player.Allgoals += name["goal_in_match"]
             player.save()

         match.Match_Details()
         return match
