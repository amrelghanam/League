from django.db import models
from django.utils.text import Truncator
from django.contrib.auth.models import User,AbstractUser

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=100)
    coach = models.CharField(max_length=100)
    founded_year = models.PositiveIntegerField()
    
    
    def __str__(self):
        return self.name


class Player(models.Model):
    POSITIONS = [
        ("GK", "Goalkeeper"),
        ("DF", "Defender"),
        ("MF", "Midfielder"),
        ("FW", "Forward"),
    ]

    team = models.ForeignKey(Team,on_delete=models.CASCADE,related_name="players")

    name = models.CharField(max_length=100)
    position = models.CharField(max_length=2, choices=POSITIONS)
    number = models.PositiveIntegerField()

    Allgoals = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
    
class Standing(models.Model):
    team = models.OneToOneField(Team, on_delete=models.CASCADE)

    played = models.IntegerField(default=0)
    won = models.IntegerField(default=0)
    draw = models.IntegerField(default=0)
    lost = models.IntegerField(default=0)
    goals_for = models.PositiveIntegerField(default=0)       
    goals_against = models.PositiveIntegerField(default=0) 
    goal_diff = models.IntegerField(default=0)   
    points = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.team.name





class Match(models.Model):
    home_team = models.ForeignKey(Team,on_delete=models.CASCADE,related_name="home_matches")
    away_team = models.ForeignKey(Team,on_delete=models.CASCADE,related_name="away_matches")

    home_score = models.PositiveIntegerField(default=0)
    away_score = models.PositiveIntegerField(default=0)
    
   # scorers = models.ManyToManyField(Player,related_name="matches_scored",blank=True)

    def Match_Details(self):

         home_standing = Standing.objects.get(team=self.home_team)
         away_standing = Standing.objects.get(team=self.away_team)

         home_standing.played += 1
         away_standing.played += 1

         home_standing.goals_for += self.home_score
         away_standing.goals_for += self.away_score

         home_standing.goals_against += self.away_score
         away_standing.goals_against += self.home_score

            #differant goal for home team
         Ingoal=home_standing.goals_for
         goalAgainst=home_standing.goals_against
         home_standing.goal_diff+= (Ingoal-goalAgainst)   
         
             #differant goal for home team
         outgoal=away_standing.goals_for
         outgoalAgainst=away_standing.goals_against
         away_standing.goal_diff+= (outgoal-outgoalAgainst)   

         if self.home_score > self.away_score:

             home_standing.won += 1
             home_standing.points += 3

             away_standing.lost += 1


         elif self.home_score < self.away_score:

              away_standing.won += 1
              away_standing.points += 3

              home_standing.lost += 1


         else:

              home_standing.draw += 1
              away_standing.draw += 1

              home_standing.points += 1
              away_standing.points += 1


         home_standing.save() 
         away_standing.save()
    
    
class playermatchscore(models.Model):

    match = models.ForeignKey(Match,on_delete=models.CASCADE,related_name="goals")

    player = models.ForeignKey(Player,on_delete=models.CASCADE,related_name="goals")
    goal_in_match = models.PositiveIntegerField(default=1)
    min_goal=models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.player.name
    
         


    
    
    
    
    
    

