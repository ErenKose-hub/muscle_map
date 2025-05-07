from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Exercise, UserExercise


def home(request):
    return render(request, "home.html")


def muscle_detail(request, muscle_name):
    exercises = Exercise.objects.filter(muscle_group__iexact=muscle_name)
    return render(
        request,
        "muscle_detail.html",
        {"muscle": muscle_name.capitalize(), "exercises": exercises},
    )


def exercise_detail(request, exercise_id):
    exercise = get_object_or_404(Exercise, id=exercise_id)
    return render(request, "exercise_detail.html", {"exercise": exercise})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()

    return render(request, "register.html", {"form": form})


@login_required
def my_exercises(request):
    user_exercises = UserExercise.objects.filter(user=request.user).select_related(
        "exercise"
    )
    exercises = [ue.exercise for ue in user_exercises]
    print(exercises)

    return render(request, "my_exercises.html", {"exercises": exercises})


@login_required
def add_to_my_exercises(request, exercise_id):
    exercise = get_object_or_404(Exercise, id=exercise_id)
    UserExercise.objects.get_or_create(user=request.user, exercise=exercise)

    return redirect("my_exercises")


@login_required
def remove_from_my_exercises(request, exercise_id):

    user_exercise = UserExercise.objects.filter(
        user=request.user, exercise_id=exercise_id
    ).first()

    if user_exercise:
        user_exercise.delete()

    return redirect("my_exercises")
