from django.urls import path
from .views import index,posts
urlpatterns = [
    path('homepage/',index,name="homepage"),
    path('posts/',posts,name="posts")
]
