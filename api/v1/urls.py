from django.urls import path, include

urlpatterns = [
    path('user/', include('api.v1.user.urls')),
    path('football-field/', include('api.v1.football_field.urls')),
    path('booking/', include('api.v1.booking.urls')),
]
