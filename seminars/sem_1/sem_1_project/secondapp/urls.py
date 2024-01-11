from django.urls import path
from .views import heads_and_tails, cube_faces, random_digits

urlpatterns = [
    path('/heads_and_tails', heads_and_tails, name='heads_and_tails'),
    path('/cube_faces', cube_faces, name='cube_faces'),
    path('/random_digits', random_digits, name='random_digits'),
]
