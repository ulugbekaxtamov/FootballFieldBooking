from django.urls import path
from . import views

app_name = 'api_football_field'
urlpatterns = [
    path('list/', views.FootballFieldListAPIView.as_view(), name='list_football_field'),
    path('create/', views.FootballFieldCreateAPIView.as_view(), name='create_football_field'),
    path('<int:id>/', views.FootballFieldRetrieveUpdateDestroyAPIView.as_view(),
         name='get_update_delete_football_field'),
]
