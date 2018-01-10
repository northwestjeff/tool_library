from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
# from library.forms import NewToolForm, NewUserForm
from library.models import User, Tool


def home(request):
    tools = Tool.objects.all()
    # # todelete = request.POST.getlist('todelete')
    #
    # # SAVES NEW TOOL
    # if request.method == "POST":
    #     if tool_form.is_valid():
    #         loan = tool_form.save(commit=False)
    #         loan.save()
    context_dict = {
        "tools": tools
    }
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
            model=model
        )

        # if tool_set.is_valid():
        #     tool_set = tool_set.save(commit=False)
        #     tool_set.save()
    return HttpResponseRedirect('')

def toolShelf(request):
    tools = Tool.objects.all()
    return render(request, 'library/toolshelf.html', {"tools": tools})

def newTool(request):
    tools = Tool.objects.all()
    return render(request, 'library/newtool.html', {"tools": tools})

def newUser(request):
    return render(request, 'library/newuser.html', {})


def delete(request):
    if request.method == 'POST':
        tool_id = request.POST.get("tool")
        if tool_id:
            # print('hello')
            tool_to_delete = Tool.objects.get(tool_id=tool_id)
            tool_to_delete.delete()

    return HttpResponse('/')











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
