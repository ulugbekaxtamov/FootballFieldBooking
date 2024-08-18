from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from apps.base.models import Base
from apps.user.models import User


class FootballField(Base):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=50)
    price_per_hour = models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(0)], default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='football_owner')

    latitude = models.DecimalField(max_digits=9, decimal_places=6, validators=[
        MinValueValidator(-90),
        MaxValueValidator(90)
    ])
    longitude = models.DecimalField(max_digits=9, decimal_places=6, validators=[
        MinValueValidator(-180),
        MaxValueValidator(180)
    ])

    def __str__(self):
        return f"{self.id} | {self.name}"


class FootballFieldImage(Base):

    def image_directory_path(instance, filename):
        return 'filed_images/football_field_{0}/{1}'.format(instance.football_field.id, filename)

    football_field = models.ForeignKey(FootballField, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_directory_path)

    def __str__(self):
        return f"{self.id} | {self.image}"
