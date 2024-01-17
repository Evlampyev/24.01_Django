from django.urls import path
from .views import index, about, base, edit_judges, delete_judge, edit_competitions

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('base/', base, name='base'),
    path('edit_judges/', edit_judges, name='edit_judges'),
    path('delete_judge/', delete_judge, name='delete_judge'),
    path('edit_competitions/', edit_competitions, name='edit_competitions'),
    # path('about/index', index, name='index'),

]
