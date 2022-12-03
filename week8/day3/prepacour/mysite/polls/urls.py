from django.urls import path
from .views import index,posts

urlpatterns = [
    path('', index, name='index'),
    path('all/', posts, name='posts'),
]