from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name="Marvel", description="Marvel Team")
        self.user = User.objects.create(name="Tony Stark", email="tony@stark.com", team=self.team)
        self.workout = Workout.objects.create(name="Super Strength", description="Strength workout")
        self.activity = Activity.objects.create(user=self.user, activity_type="Running", duration_minutes=30, date="2024-01-01")
        self.leaderboard = Leaderboard.objects.create(user=self.user, score=100, rank=1)

    def test_user_team(self):
        self.assertEqual(self.user.team.name, "Marvel")

    def test_activity_user(self):
        self.assertEqual(self.activity.user.email, "tony@stark.com")

    def test_leaderboard_user(self):
        self.assertEqual(self.leaderboard.user.name, "Tony Stark")

    def test_workout_name(self):
        self.assertEqual(self.workout.name, "Super Strength")
