from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import F

from todo.forms import TodoForm
from .models import Todo


def todo_list(request):
    todos = Todo.objects.order_by('priority', F('expiration').asc(nulls_last=True)).exclude(is_done=True)
    contexts = {
        'todos': todos,
    }
    return render(request, 'todo/todo_list.html', contexts)


def todo_detail(request, pk, ask_delete=False):
    try:
        todo = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return HttpResponse('Todo #{} does not exist'.format(pk))
    # ask_delete 값이 있으면 모달 띄워줌
    if ask_delete:
        context = {
            'todo': todo,
            'ask_delete': True,
        }
        return render(request, 'todo/todo_detail.html', context)
    context = {
        'todo': todo,
        'ask_delete': False,
    }
    return render(request, 'todo/todo_detail.html', context)


def todo_add(request):
    if request.method == 'POST':
        form = TodoForm(request.POST, request.FILES)
        if form.is_valid():
            todo = form.save()
            return redirect('todo_detail', pk=todo.pk)
    form = TodoForm()
    context = {
        'form': form,
    }
    return render(request, 'todo/todo_create.html', context)


def todo_delete(request, pk):
    url = request.META['HTTP_REFERER']
    if request.method == 'POST':
        todo = Todo.objects.get(pk=pk)
        todo.delete()
        return redirect('main')
    return redirect(url)


def todo_change(request, pk):
    try:
        todo = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return HttpResponse('Todo #{} does not exist'.format(pk))
    if request.method == 'POST':
        form = TodoForm(request.POST, request.FILES)
        if form.is_valid():
            new_todo = form.save(commit=False)
            todo.swap_content(new_todo)
            return redirect('todo_detail', pk=todo.pk)
    initial = {
        'title': todo.title,
        'content': todo.content,
        'expiration': todo.expiration,
        'priority': Todo.CHOICES[todo.priority-1],
    }
    form = TodoForm(initial=initial)
    context = {
        'form': form,
    }
    return render(request, 'todo/todo_change.html', context)


def todo_complete(request, pk):
    try:
        todo = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return HttpResponse(f'Todo #{pk} dose not exist')
    todo.done()
    return redirect('main')
