from django.urls import path
from . import views
from .auth_views import (
    CustomRegisterView,
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    CustomTokenVerifyView,
    logout_view
)

app_name = 'api_user'
urlpatterns = [
    # AUTH
    path('register/', CustomRegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', CustomTokenVerifyView.as_view(), name='token_verify'),
    path('logout/', logout_view, name='logout'),

]
