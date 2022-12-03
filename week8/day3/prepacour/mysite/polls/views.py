from django.shortcuts import render
from .models import Person, Post # import the models from polls/models.py

#person = Person.objects.all()[4]
person = Person.objects.filter(first_name="Maria", last_name = "Fez").first()
def index(request):
    context = {
        'page_title' : "Homepage",
        'user' : person
    }
    return render(request, 'posts/homepage.html', context)

def posts(request):
    print(Post.objects.all())
    print("OK")
    context = {
        'posts' : Post.objects.all,
        'user' : person,
        'page_title' : "Posts"
    }
    return render(request, 'posts/posts.html', context)

