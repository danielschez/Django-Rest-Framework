from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View

class HelloWorld(View):
    def get(self, request):
        data = {
            'name': 'Daniel Hernandez Sanchez',
            'age': 25,
            'codes': ['Python', 'Django']
        }
        return render(request, 'hello_world.html', context=data)
