from django.urls import path
from .views import myGif
urlpatterns = [
    path('addNewGif/', myGif,name="home page")
]