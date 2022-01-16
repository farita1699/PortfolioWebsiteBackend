from .serializers import ProjectSerializer
from .models import Project
from rest_framework import viewsets, permissions

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = ProjectSerializer

class FeaturedProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.filter(featured="True").all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = ProjectSerializer

class WebProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.filter(cartegory="Web App").all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = ProjectSerializer

class HealthProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.filter(cartegory="Health Science").all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = ProjectSerializer

class MechatronicsProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.filter(cartegory="Mechatronics").all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = ProjectSerializer

class OtherProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.filter(cartegory="Other").all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = ProjectSerializer
