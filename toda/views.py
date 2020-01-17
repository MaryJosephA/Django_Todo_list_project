from django.http import HttpResponse
from django.shortcuts import render, redirect

from todo.models import Todo_List


def login(request):
    return render(request, 'session/new.html')

def signin(request):
    username = request.POST["username"]
    password = request.POST["password"]
    if username == 'mary' and password == 'password':
        return redirect(index)
    else:
        return render(request, 'session/new.html', {'some_flag': True})

def index(request):
    return render(request, 'todo/index.html', {'items': Todo_List.objects.all})

def create_todo(request):
    q = Todo_List(list=request.POST["todo_list"])
    q.save()

    return redirect(index)

def delete(request, id):
    instance = Todo_List.objects.get(id=id)
    instance.delete()

    return redirect(index)




