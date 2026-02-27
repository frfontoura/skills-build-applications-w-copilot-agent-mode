from djongo import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)
    # outros campos relevantes

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ArrayReferenceField(to=User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=50)
    duration = models.IntegerField()  # minutos
    calories = models.FloatField()
    date = models.DateTimeField()

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()

class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    score = models.FloatField()
    updated_at = models.DateTimeField(auto_now=True)
