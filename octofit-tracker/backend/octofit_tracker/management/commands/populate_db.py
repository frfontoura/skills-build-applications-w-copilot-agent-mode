from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models
from octofit_tracker import settings
from django.db import connection

from django.apps import apps

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        Team = self.get_or_create_team_model()
        Activity = self.get_or_create_activity_model()
        Leaderboard = self.get_or_create_leaderboard_model()
        Workout = self.get_or_create_workout_model()

        # Clean up collections
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Users
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='pass', first_name='Tony', last_name='Stark', team=marvel),
            User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='pass', first_name='Peter', last_name='Parker', team=marvel),
            User.objects.create_user(username='batman', email='batman@dc.com', password='pass', first_name='Bruce', last_name='Wayne', team=dc),
            User.objects.create_user(username='wonderwoman', email='wonderwoman@dc.com', password='pass', first_name='Diana', last_name='Prince', team=dc),
        ]

        # Activities
        activities = [
            Activity.objects.create(user=users[0], type='run', duration=30, distance=5),
            Activity.objects.create(user=users[1], type='cycle', duration=45, distance=20),
            Activity.objects.create(user=users[2], type='swim', duration=60, distance=2),
            Activity.objects.create(user=users[3], type='run', duration=25, distance=4),
        ]

        # Workouts
        workouts = [
            Workout.objects.create(name='Morning Cardio', description='Cardio for all heroes', suggested_for_team=marvel),
            Workout.objects.create(name='Strength Training', description='Strength for DC heroes', suggested_for_team=dc),
        ]

        # Leaderboard
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))

    def get_or_create_team_model(self):
        class Team(models.Model):
            name = models.CharField(max_length=100, unique=True)
            class Meta:
                app_label = 'octofit_tracker'
        return Team

    def get_or_create_activity_model(self):
        User = get_user_model()
        class Activity(models.Model):
            user = models.ForeignKey(User, on_delete=models.CASCADE)
            type = models.CharField(max_length=50)
            duration = models.IntegerField()
            distance = models.FloatField()
            class Meta:
                app_label = 'octofit_tracker'
        return Activity

    def get_or_create_leaderboard_model(self):
        Team = self.get_or_create_team_model()
        class Leaderboard(models.Model):
            team = models.ForeignKey(Team, on_delete=models.CASCADE)
            points = models.IntegerField()
            class Meta:
                app_label = 'octofit_tracker'
        return Leaderboard

    def get_or_create_workout_model(self):
        Team = self.get_or_create_team_model()
        class Workout(models.Model):
            name = models.CharField(max_length=100)
            description = models.TextField()
            suggested_for_team = models.ForeignKey(Team, on_delete=models.CASCADE)
            class Meta:
                app_label = 'octofit_tracker'
        return Workout
