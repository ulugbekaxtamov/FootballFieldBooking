from django.urls import path
from .views import BookingListAPIView, BookingCreateAPIView, BookingRetrieveUpdateDestroyView

app_name = 'api_booking'
urlpatterns = [
    path('list/', BookingListAPIView.as_view(), name='booking_list'),
    path('create/', BookingCreateAPIView.as_view(), name='booking_create'),
    path('<int:pk>/', BookingRetrieveUpdateDestroyView.as_view(), name='booking_detail'),
]
