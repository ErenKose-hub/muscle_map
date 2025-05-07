from django.contrib import admin
from django.urls import path
from exercises import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("muscle/<str:muscle_name>/", views.muscle_detail, name="muscle_detail"),
    path(
        "login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"
    ),
    path("logout/", auth_views.LogoutView.as_view(next_page="home"), name="logout"),
    path("register/", views.register, name="register"),
    path("my-exercises/", views.my_exercises, name="my_exercises"),
    path(
        "add/<int:exercise_id>/", views.add_to_my_exercises, name="add_to_my_exercises"
    ),
    path(
        "remove/<int:exercise_id>/",
        views.remove_from_my_exercises,
        name="remove_from_my_exercises",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
