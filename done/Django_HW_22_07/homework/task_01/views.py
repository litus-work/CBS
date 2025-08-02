from django.http import HttpResponse
from django.shortcuts import render

# Заданный список дел
lets_do_it = [
    {'priority': 100, 'task': 'Скласти перелік справ'},
    {'priority': 150, 'task': 'Вивчати Django'},
    {'priority': 1, 'task': 'Подумати про сенс життя'},
]

def todo_view(request):
    return render(request, "task_01/todo.html", {"tasks": lets_do_it})