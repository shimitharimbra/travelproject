from django.shortcuts import render
from.models import place,people


def demo(request):
    obj1=place.objects.all()
    obj2 = people.objects.all()

    return render(request,"index.html",{'result1':obj1,'result2':obj2})
