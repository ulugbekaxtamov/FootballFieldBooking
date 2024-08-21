from django_filters.rest_framework import DjangoFilterBackend
from django.db import models
from django.db.models import F, Q, ExpressionWrapper, FloatField, Value

from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import generics, permissions
from django.db.models.functions import Cast

from apps.football_field.models import FootballField

from .permissions import CreatePermission, UpdateDeleteObjectPermission
from .serializers import FootballFieldSerializer
from .filters import FootballFieldFilter, haversine_distance
from .haversine import Haversine, Asin, Sqrt, Power, Cos, Sin, Radians
from django.db.models import F, Func, Value, FloatField, ExpressionWrapper


# Example 1
# def distance_calculator(queryset, lat, lon):
#     distances = []
#     for obj in queryset:
#         try:
#             dist = haversine_distance(lat, lon, float(obj.latitude), float(obj.longitude))
#             distances.append((obj, dist))
#         except Exception as e:
#             print(f"Error calculating distance for object {obj.id}: {e}")
#             continue
#     distances.sort(key=lambda x: x[1])
#     return [obj for obj, _ in distances]


class FootballFieldListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FootballFieldSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_class = FootballFieldFilter

    def get_queryset(self):
        queryset = FootballField.objects.all()

        latitude = self.request.query_params.get('latitude')
        longitude = self.request.query_params.get('longitude')
        if latitude and longitude:
            latitude = float(latitude)
            longitude = float(longitude)

            # FOR Example 2
            # queryset = FootballField.objects.annotate(
            #     distance=ExpressionWrapper(
            #         6371 * 2 * Asin(
            #             Sqrt(
            #                 Power(Sin(Radians(F('latitude') - Value(latitude))) / 2, 2) +
            #                 Cos(Radians(F('latitude'))) * Cos(Radians(Value(latitude))) *
            #                 Power(Sin(Radians(F('longitude') - Value(longitude))) / 2, 2)
            #             )
            #         ),
            #         output_field=FloatField()
            #     )
            # ).order_by('distance')

            # FOR Example 3
            queryset = FootballField.objects.with_distance(latitude, longitude).order_by('-distance')

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
