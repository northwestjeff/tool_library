from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


from library.models import User, Tool



def home(request):
    tools = Tool.objects.all()
    return render(request, 'library/home.html', {"tools": tools})


    def post(self, request):

        if form.is_valid():
            text = form.cleaned_data['post']

        args

        return render(request, 'library/home.html', {"tools": tools})




