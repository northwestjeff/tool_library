from django.shortcuts import render
from library.models import User, Tool



def home(request):
    tools = Tool.objects.all()
    return render(request, 'library/home.html', {"tools": tools})

