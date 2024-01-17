from django.urls import path
from .views import hello, HelloWorld
from .views import year_post, MonthPost, post_detail

urlpatterns = [
    path('hello/', hello, name='hello'),
    path('hello2/', HelloWorld.as_view(), name='hello2'),
    path('posts/<int:year>/', year_post, name='year_post'),
    path('posts/<int:year>/<int:month>/', MonthPost.as_view(), name='month_post'),
    path('posts/<int:year>/<int:month>/<slug:slug>/', post_detail, name='post_detail'),

]
