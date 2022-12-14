from django.urls import include,path #path function
from . import views # . is shorthand for the current directory

# one urlpattern per line
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')), # include the urls.py from the polls application
]
# '' : empty string and /
# views.index : index function in views.py
# name='index' : name of the route
