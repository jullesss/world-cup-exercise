from django.urls import path
from .views import TeamView, TeamViewDetailed

urlpatterns = [
    path("teams/", TeamView.as_view()),
    path("teams/<int:team_id>/", TeamViewDetailed.as_view()),
]
