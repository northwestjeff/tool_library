from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from library.forms import NewToolForm, NewUserForm
from library.models import User, Tool


def home(request):
    tools = Tool.objects.all()
    tool_form = NewToolForm(request.POST or None)
    # # todelete = request.POST.getlist('todelete')
    #
    # # SAVES NEW TOOL
    # if request.method == "POST":
    #     if tool_form.is_valid():
    #         loan = tool_form.save(commit=False)
    #         loan.save()
    context_dict = {
        "tools": tools,
        "tool_form": tool_form
    }
    return render(request, 'library/home.html', context_dict)


def add(request):
    if request.method == "POST":
        tool_id = request.POST['tool_id']
        name = request.POST['name']
        make = request.POST['make']
        type = request.POST['type']

        Tool.objects.create(
            tool_id=tool_id,
            name=name,
            make=make,
            type=type
        )

        # if tool_set.is_valid():
        #     tool_set = tool_set.save(commit=False)
        #     tool_set.save()
    return HttpResponseRedirect('')


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
