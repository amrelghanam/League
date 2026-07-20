from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView,ListCreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import Team, Player,Standing,Match
from .serializers import TeamSerializer, PlayerSerializer,StandingSerializer,TopScorerSerializer,MatchSerializer

class TeamViewSet(ModelViewSet):

    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def get_permissions(self):

        if self.action == "list" or self.action == "retrieve":
            return [AllowAny()]
        
        return [IsAuthenticated()]

    
class PlayerViewSet(ModelViewSet):

    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


    def get_permissions(self):

        if self.action == "list" or self.action == "retrieve":
            return [AllowAny()]

        return [IsAuthenticated()]
 
 

class TopScorerAPIView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):

        player = Player.objects.all().order_by("-Allgoals").first()

        serializer = TopScorerSerializer(player)

        return Response(serializer.data)   


class MatchListCreateView(ListCreateAPIView):

    queryset = Match.objects.all()
    serializer_class = MatchSerializer


    def get_permissions(self):

        if self.request.method == "GET":
            return [AllowAny()]

        return [IsAuthenticated()]
class StandingListAPIView(ListAPIView):
    
    permission_classes = [AllowAny]
    queryset = Standing.objects.all().order_by("-points")
    serializer_class = StandingSerializer
    