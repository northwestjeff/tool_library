from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
# from library.forms import NewToolForm, NewUserForm
from library.models import User, Tool, Comment, Activity


def home(request):
    tools = Tool.objects.all()
    return render(request, 'library/home.html', {"tools": tools})


def add(request):
    if request.method == "POST":
        tool_id = request.POST['tool_id']
        description = request.POST['description']
        parts = request.POST['parts']
        brand = request.POST['brand']
        model = request.POST['model']
        Tool.objects.create(
            tool_id=tool_id,
            description=description,
            parts=parts,
            brand=brand,
            model=model)
    return HttpResponseRedirect('')


def update(request):
    if request.method == "POST":
        tool_id = request.POST['tool_id']
        description = request.POST['description']
        parts = request.POST['parts']
        brand = request.POST['brand']
        model = request.POST['model']
        try:
            tool = Tool.objects.get(tool_id=tool_id)
            tool.description = description
            tool.parts = parts
            tool.brand = brand
            tool.model = model
            tool.save()
        except:
            return render(request, 'library/home.html', status=500)

    tools = Tool.objects.all()
    return render(request, 'library/home.html', {"tools": tools})


def toolShelf(request):
    tools = Tool.objects.all()
    # tools = []
    return render(request, 'library/tools.html', {"tools": tools})


def editTools(request):
    tools = Tool.objects.all()
    return render(request, 'library/edittools.html', {'tools': tools})


def newTool(request):
    tools = Tool.objects.all()
    return render(request, 'library/newtool.html', {"tools": tools})


def newUserForm(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        zip_code = request.POST.get('zip')
        # User.objects.create(
        #     user.first_name=first_name,
        #     user.last_name=last_name,
        #     email=email,
        #     zip=zip_code)
    return render(request, 'library/newuser.html', {})


def adminViewUser(request):
    users = User.objects.all()
    return render(request, 'library/users.html', {"users": users})


def viewUser(request, id):
    user = User.objects.get(id=id)
    return render(request, 'library/user_page.html', {"user": user})


def delete(request):
    if request.method == 'POST':
        tool_id = request.POST.get("tool_id")
        if tool_id:
            # print('hello')
            tool_to_delete = Tool.objects.get(tool_id=tool_id)
            tool_to_delete.delete()
    return HttpResponse('/')


def viewTool(request, tool_id):
    tool = Tool.objects.get(tool_id=tool_id)
    users = User.objects.all()
    return render(request, 'library/tool.html', {"tool": tool,
                                                 "users": users
                                                 })

def updateTool(request, tool_id):
    # tool = request.POST.get("tool_id")
    tool = Tool.objects.get(tool_id=tool_id)
    return render(request, 'library/toolupdate.html', {"tool": tool})


def checkoutTool(request):
    if request.method == 'POST':
        tool_id = request.POST.get("tool_id")
        tool = Tool.objects.get(tool_id=tool_id)
        user_id = request.POST.get("user")
        user = User.objects.get(user_id=user_id)
        tool.available = False
        tool.user_id = user
        tool.save()
    return render(request, 'library/home.html', {})






    # def post(self, request):
    #
    #     if form.is_valid():
    #         text = form.cleaned_data['post']
    #
    #     args
    #
    #     return render(request, 'library/home.html', {"tools": tools})
    #
    #
