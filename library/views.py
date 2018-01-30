import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
# from library.forms import NewToolForm, NewUserForm
from library.models import User, Tool, Comment, Activity
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView


def home(request):
    tools = Tool.objects.all()
    if request.user.is_authenticated():
        current_user = request.user
        return render(request, 'library/home.html', {"tools": tools,
                                                     "current_user": current_user})
    else:
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
        Activity.objects.create(
            action='New Tool',
            date_in=datetime.datetime.now(),
            # member=user.username,
            staff=request.user.username,
            tool=Tool.objects.get(tool_id=tool_id),
        )
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
    tools = Tool.objects.filter(available=True)
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
        username = request.POST.get('username')
        password = request.POST.get('password')
        zip_code = request.POST.get('zip')
        User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
            password=password,
            zip=zip_code,
            is_member=True
        )
        Activity.objects.create(
            action='New Member',
            member=User.objects.get(username=username),
            date_in=datetime.datetime.now(),
        )
    return render(request, 'library/newuser.html', {})


def adminViewUser(request):
    users = User.objects.all()
    return render(request, 'library/users.html', {"users": users})


def viewUser(request, id):
    user = User.objects.get(id=id)
    tools = Tool.objects.filter(user=user)
    return render(request, 'library/user_page.html', {"user": user,
                                                      "tools": tools
                                                      })

def viewAccount(request):
    user = User.objects.get(id=request.user.id)
    tools = Tool.objects.filter(user=user)
    return render(request, 'library/user_page.html', {"user": user,
                                                      "tools": tools
                                                      })


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
        user = User.objects.get(id=user_id)
        tool.available = False
        tool.user_id = user
        tool.save()
        Activity.objects.create(
            action='Checkout',
            date_out=datetime.datetime.now(),
            member=User.objects.get(id=user.id),
            staff=User.objects.get(id=request.user.id),
            tool=Tool.objects.get(tool_id=tool_id)
        )
    return render(request, 'library/home.html', {})

def returnTool(request):
    if request.method == 'POST':
        tool_id = request.POST.get("tool_id")
        tool = Tool.objects.get(tool_id=tool_id)
        borrower_id = request.POST.get("borrower_id")
        user = User.objects.get(id=borrower_id)
        tool.available = True
        tool.user_id = None
        tool.save()
        Activity.objects.create(
            action='Return',
            date_in=datetime.datetime.now(),
            member=User.objects.get(id=user.id),
            staff=User.objects.get(username=request.user.username),
            tool=Tool.objects.get(tool_id=tool_id)
        )
    return render(request, 'string', {})


def viewActivityLog(request):
    log = Activity.objects.all()
    return render(request, 'library/activitylog.html', {"log": log})


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
