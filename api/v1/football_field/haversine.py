from django.db.models import Func, F, ExpressionWrapper, FloatField
from django.db.models.functions import Cast
from django.db.models.functions import Cos, Sin, ASin, Radians


# For example 2
class Radians(Func):
    function = 'RADIANS'
    template = '%(function)s(%(expressions)s)'


class Power(Func):
    function = 'POWER'
    template = '%(function)s(%(expressions)s)'


class Sin(Func):
    function = 'SIN'
    template = '%(function)s(%(expressions)s)'


class Cos(Func):
    function = 'COS'
    template = '%(function)s(%(expressions)s)'


class Sqrt(Func):
    function = 'SQRT'
    template = '%(function)s(%(expressions)s)'


class Asin(Func):
    function = 'ASIN'
    template = '%(function)s(%(expressions)s)'


# DRAFT
class Haversine(Func):
    function = ''
    template = '''
        6371 * 2 * ASIN(
            SQRT(
                POWER(SIN(RADIANS(%(lat2)s - %(lat1)s) / 2), 2) +
                COS(RADIANS(%(lat1)s)) * COS(RADIANS(%(lat2)s)) *
                POWER(SIN(RADIANS(%(lon2)s - %(lon1)s) / 2), 2)
            )
        )
    '''

    def __init__(self, lat1, lon1, lat2, lon2, **extra):
        super().__init__(
            template=self.template % {
                'lat1': '%(expressions)s[0]',
                'lat2': '%(expressions)s[1]',
                'lon1': '%(expressions)s[2]',
                'lon2': '%(expressions)s[3]',
            },
            **extra
        )
        self.set_source_expressions([lat1, lat2, lon1, lon2])
