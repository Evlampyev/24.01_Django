from django.urls import path
from .views import index, about, base, edit_judges, delete_judge, edit_competitions, \
    add_judge, add_competition, edit_judge, competition_activate, delete_competition, \
    edit_competition

urlpatterns = [

    path('edit_competitions/', edit_competitions, name='edit_competitions'),
    path('add_competition/', add_competition, name='add_competition'),
    path('delete_competition/<int:pk>/', delete_competition, name='delete_competition'),
    path('edit_competition/<int:pk>/', edit_competition, name='edit_competition'),
    path('competition_activate/<int:pk>/', competition_activate, name='competition_activate'),
    # path('about/index', index, name='index'),

]
