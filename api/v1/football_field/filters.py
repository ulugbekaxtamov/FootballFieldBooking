from django.db.models import Q, F
from django_filters import rest_framework as filters
from django.utils import timezone
from math import radians, sin, cos, sqrt, atan2

from apps.football_field.models import FootballField
from .haversine import Haversine, Asin, Sqrt, Power, Cos, Sin, Radians
from django.db.models import F, Func, Value, FloatField, ExpressionWrapper


# Example 1
def haversine_distance(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    r = 6371  # Radius of earth in kilometers
    return r * c


class FootballFieldFilter(filters.FilterSet):
    start_time = filters.DateTimeFilter(method='filter_by_time')
    end_time = filters.DateTimeFilter(method='filter_by_time')
    latitude = filters.NumberFilter(method='filter_by_location')
    longitude = filters.NumberFilter(method='filter_by_location')
    name = filters.CharFilter(lookup_expr='icontains')
    address = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = FootballField
        fields = ['start_time', 'end_time', 'latitude', 'longitude', 'name', 'address']

    def filter_by_time(self, queryset, name, value):
        start_time = self.data.get('start_time')
        end_time = self.data.get('end_time')

        if start_time and end_time:
            start_time = timezone.make_aware(timezone.datetime.fromisoformat(start_time))
            end_time = timezone.make_aware(timezone.datetime.fromisoformat(end_time))

            queryset = queryset.exclude(
                Q(booking__start_time__lt=end_time) & Q(booking__end_time__gt=start_time)
            )

        return queryset

    def filter_by_location(self, queryset, name, value):
        latitude = self.data.get('latitude')
        longitude = self.data.get('longitude')

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

            # For Example 3
            queryset = FootballField.objects.with_distance(latitude, longitude).order_by('distance')

        return queryset
