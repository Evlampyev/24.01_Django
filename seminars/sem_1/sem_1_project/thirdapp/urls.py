from django.urls import path
from .views import third_index, heads_and_tails, cube_faces, random_digits, author_post, \
    post_view, games_choose, add_author, add_post

urlpatterns = [
    path('', third_index, name='third_index'),
    path('heads_and_tails/<int:count>/', heads_and_tails, name='heads_and_tails'),
    path('cube_faces/<int:count>/', cube_faces, name='cube_faces'),
    path('random_digits/<int:count>/', random_digits, name='random_digits'),
    path('author_post/<int:author_id>/', author_post, name='author_post'),
    path('post/<int:post_id>/', post_view, name='post_view'),
    path('games/', games_choose, name='games'),
    path('add_author/', add_author, name='add_author'),
    path('add_post/', add_post, name='add_post'),


]
