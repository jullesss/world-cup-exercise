from utils import data_processing
from rest_framework.views import APIView, Request, Response, status
from .models import Team
from django.forms.models import model_to_dict


class TeamView(APIView):
    def get(self, request: Request) -> Response:
        teams = Team.objects.all()

        team_list = []
        for team in teams:
            team_dict = model_to_dict(team)
            team_list.append(team_dict)

        return Response(team_list, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        team = Team.objects.create(**request.data)
        team_dict = model_to_dict(team)

        return Response(team_dict, status.HTTP_201_CREATED)
