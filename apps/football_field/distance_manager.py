from django.db.models import Func, F, ExpressionWrapper, FloatField
from django.db.models.functions import Cos, Sin, ASin, Radians, Cast
from django.db import models


class Sin(Func):
    function = 'SIN'


class Cos(Func):
    function = 'COS'


class Acos(Func):
    function = 'ACOS'


class Radians(Func):
    function = 'RADIANS'


# For Example 3
class WithDistanceManager(models.Manager):
    def with_distance(self, latitude, longitude):
        radlat = Radians(latitude)
        radlong = Radians(longitude)
        radflat = Radians(F('latitude'))
        radflong = Radians(F('longitude'))

        expression = 6371.0 * Acos(
            Cos(radlat) * Cos(radflat) * Cos(radflong - radlong) +
            Sin(radlat) * Sin(radflat)
        )

        return self.get_queryset().annotate(
            distance=ExpressionWrapper(
                expression,
                output_field=FloatField()
            )
        )
