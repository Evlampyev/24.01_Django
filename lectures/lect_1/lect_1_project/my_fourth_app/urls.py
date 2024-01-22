from django.urls import path
from .views import user_form, many_fields_form, upload_image

urlpatterns = [
    path('user/add/', user_form, name='user_form'),
    path('forms/', many_fields_form, name='many_fields_form'),
    path('upload/', upload_image, name='upload_image'),

]
