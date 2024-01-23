from django.urls import path
from .views import index, about, base, edit_judges, delete_judge, edit_competitions, \
    add_judge, add_competition, edit_judge, competition_activate, delete_competition, \
    edit_competition

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('base/', base, name='base'),
    path('edit_judges/', edit_judges, name='edit_judges'),
    path('edit_judge/<int:pk>/', edit_judge, name='edit_judge'),
    path('delete_judge/<int:pk>/', delete_judge, name='delete_judge'),
    path('add_judge/', add_judge, name='add_judge'),
    path('edit_competitions/', edit_competitions, name='edit_competitions'),
    path('add_competition/', add_competition, name='add_competition'),
    path('delete_competition/<int:pk>/', delete_competition, name='delete_competition'),
    path('edit_competition/<int:pk>/', edit_competition, name='edit_competition'),
    path('competition_activate/<int:pk>/', competition_activate, name='competition_activate'),
    # path('about/index', index, name='index'),

]
