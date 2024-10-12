from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Client, ServiceProvider, Experience, Skill
from .serializers import ClientSerializer, ServiceProviderSerializer, ExperienceSerializer, SkillSerializer
from rest_framework.exceptions import PermissionDenied

# CLIENT VIEW
class ClientListCreateView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Assign the authenticated user to the client


class ExperienceListCreateView(generics.ListCreateAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Assign the authenticated user to the experience


class SkillListCreateView(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Assign the authenticated user to the skill


class ServiceProviderListCreateView(generics.ListCreateAPIView):
    queryset = ServiceProvider.objects.all()
    serializer_class = ServiceProviderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Assign the authenticated user to the service provider


# Experience Update and Delete Views
class ExperienceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        obj = super().get_object()
        if obj.user != self.request.user:  # Only allow the owner to access
            raise PermissionDenied("You do not have permission to access this experience.")
        return obj


class SkillDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        obj = super().get_object()
        if obj.user != self.request.user:  # Only allow the owner to access
            raise PermissionDenied("You do not have permission to access this skill.")
        return obj


class ServiceProviderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceProvider.objects.all()
    serializer_class = ServiceProviderSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        obj = super().get_object()
        if obj.user != self.request.user:  # Only allow the owner to access
            raise PermissionDenied("You do not have permission to access this service provider.")
        return obj
