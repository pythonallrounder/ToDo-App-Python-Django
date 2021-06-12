from django.shortcuts import render,redirect
from todo.models import *
from django.utils import timezone

# Create your views here.


def  index(request):
    todo_items = todo.objects.all().order_by("-added_date")
    
    return render(request,'index.html',{'todo_items' : todo_items})


def add_item(request):
    current_date = timezone.now()
    content = request.POST["content"]
    author_name = request.POST['author']
    created_obj = todo.objects.create(added_date = current_date, text= content,author_name=author_name)
    return redirect('/')
    
def delete_todo(request,todo_id):
    todo.objects.get(id=todo_id).delete()
    return redirect('/')

