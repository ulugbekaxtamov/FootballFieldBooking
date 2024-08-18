from django_filters.rest_framework import DjangoFilterBackend
from django.db import models

from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import generics, permissions

from apps.football_field.models import FootballField

from .permissions import CreatePermission, UpdateDeleteObjectPermission
from .serializers import FootballFieldSerializer
from .filters import FootballFieldFilter, haversine_distance


def distance_calculator(queryset, lat, lon):
    distances = []
    for obj in queryset:
        try:
            dist = haversine_distance(lat, lon, float(obj.latitude), float(obj.longitude))
            distances.append((obj, dist))
        except Exception as e:
            print(f"Error calculating distance for object {obj.id}: {e}")
            continue
    distances.sort(key=lambda x: x[1])
    return [obj for obj, _ in distances]


class FootballFieldListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FootballFieldSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = FootballFieldFilter

    def get_queryset(self):
        queryset = FootballField.objects.all()

        latitude = self.request.query_params.get('latitude')
        longitude = self.request.query_params.get('longitude')
        if latitude and longitude:
            latitude = float(latitude)
            longitude = float(longitude)
            queryset = queryset.annotate(
                distance=models.FloatField()
            )
            queryset = distance_calculator(queryset, latitude, longitude)

        return queryset


class FootballFieldCreateAPIView(generics.CreateAPIView):
    permission_classes = [CreatePermission]
    serializer_class = FootballFieldSerializer
    queryset = FootballField.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FootballFieldRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FootballField.objects.all()
    serializer_class = FootballFieldSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, UpdateDeleteObjectPermission]
