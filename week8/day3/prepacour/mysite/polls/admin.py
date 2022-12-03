from django.contrib import admin

from .models import Person,ImageProfile,Post #import the Person model

# Register your models here.
admin.site.register(Person)
admin.site.register(Post)
admin.site.register(ImageProfile)
