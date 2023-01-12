from django.shortcuts import render
from phonenumber_field.modelfields import PhoneNumberField
from .models import Person
# Create your views here.

def phonenumber(request,number):
    person=Person.objects.all()
    for i in person:
        x=str(i.phoneNumber)
        if x==number:
            print(i.phoneNumber)
            interest=i
    print(interest)
    context={
        'x': interest
    }
    return render(request,"phoneNumber.html",context)

def name(request,nom):
    context = {
        'person':Person.objects.all(),
        'nom': nom,
    }
    return render(request,"name.html",context)
