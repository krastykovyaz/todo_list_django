from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem

def todoView(request):
    all_todo_item = TodoItem.objects.all()
    return render(request, 'todo.html',{'all_items' : all_todo_item})
# def todoView(request):
#     return render(request, 'todo.html')

def addTodo(request):
    # create
    # save
    # redirect
    c = request.POST['content']
    new_item = TodoItem(content=c)
    new_item.save()
    return HttpResponseRedirect('/todo/')

def delTodo(request, todo_id):
    item_to_del = TodoItem.objects.get(id=todo_id)
    item_to_del.delete()
    return HttpResponseRedirect('/todo/')
