from django.urls import path
from .views import index, about, base, edit_judges

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('base/', base, name='base'),
    path('edit_judges/', edit_judges, name='edit_judges'),
    # path('about/index', index, name='index'),

]
