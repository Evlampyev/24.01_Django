from django.urls import path
from .views import index, about, base, edit_judges, delete_judge, add_judge, edit_judge

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('base/', base, name='base'),
    path('edit_judges/', edit_judges, name='edit_judges'),
    path('edit_judge/<int:pk>/', edit_judge, name='edit_judge'),
    path('delete_judge/<int:pk>/', delete_judge, name='delete_judge'),
    path('add_judge/', add_judge, name='add_judge'),

]
