from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.
def index(request):
    #return HttpResponse('my_to_do_app first page')
    # my_to_do_app_todo 테이블의 모든 데이터를 todos에 저장
    todos = Todo.objects.all()
    content = {'todos': todos}
    return render(request, 'my_to_do_app/index.html', content)

def createTodo(request):
    #return HttpResponse('createTodo')
    user_input_str = request.POST['todoContent']
    new_todo = Todo(content=user_input_str)
    new_todo.save()     # my_to_do_app_todo 테이블에 저장
    #return HttpResponse('create Todo=' + user_input_str)
    return HttpResponseRedirect(reverse('index'))

def deleteTodo(request):
    done_todo_id = request.GET['todoNum']
    print('완료한 todo의 id', done_todo_id)
    todo = Todo.objects.get(id=done_todo_id)
    todo.delete()       # my_to_do_app_todo 테이블에서 해당 데이터 삭제
    return HttpResponseRedirect(reverse('index'))

def boolTodo(request):
    done_todo_id = request.GET['todoNum']
    print('완료한 todo의 id', done_todo_id)
    todo = Todo.objects.get(id=done_todo_id)
    todo.isDone = True
    todo.save()
    return HttpResponseRedirect(reverse('index'))



