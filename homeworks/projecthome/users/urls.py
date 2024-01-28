from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import LoginUser

app_name = "users"

urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
LOGOUT_REDIRECT_URL = 'home'
