from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem

# Create your views here.
# request is input
def todoView(request):
    all_todo_items = TodoItem.objects.all()
    return render(request, 'todo.html',
        {'all_items': all_todo_items})

def addTodo(request):
    #create new todo all_items
    new_item = TodoItem(content = request.POST['content'])
    # saving it
    new_item.save()
    # redirect the brower to og url which is /todo/
    return HttpResponseRedirect('/todo/')

def deleteTodo(request, todo_id):
    # retrieve todo item object that matches todo_id
    item_to_delete = TodoItem.objects.get(id=todo_id)
    #deleting it
    item_to_delete.delete();
    # redirect the brower to og url which is /todo/
    return HttpResponseRedirect('/todo/')
