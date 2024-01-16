from django.urls import path
from .views import index, about, base

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('base/', base, name='base'),
    # path('about/index', index, name='index'),

]
