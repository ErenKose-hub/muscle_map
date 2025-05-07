from django.db import models
from django.contrib.auth.models import User


class MuscleGroup(models.TextChoices):
    CHEST = "Gogus", "Gogus"
    BACK = "Sirt", "Sirt"
    LEGS = "Bacak", "Bacak"
    SHOULDERS = "Omuz", "Omuz"
    ARMS = "Kollar", "Kollar"
    CORE = "Karin", "Karin"


class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    muscle_group = models.CharField(
        max_length=20,
        choices=MuscleGroup.choices,
        default=MuscleGroup.CHEST,
    )
    image = models.ImageField(upload_to="exercise_images/", blank=True, null=True)

    def __str__(self):
        return self.name


class UserExercise(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_exercises"
    )
    exercise = models.ForeignKey(
        Exercise, on_delete=models.CASCADE, related_name="user_exercises"
    )

    def __str__(self):
        return f"{self.user.username} - {self.exercise.name}"
