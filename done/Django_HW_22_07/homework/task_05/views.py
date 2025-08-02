from django.shortcuts import render

lets_do_it = [
    {'priority': 100, 'task': 'Скласти перелік справ'},
    {'priority': 150, 'task': 'Вчити Django'},
    {'priority': 1, 'task': 'Подумати про сенс життя'}
]

def todo_view(request):
    sorted_tasks = sorted(lets_do_it, key=lambda x: x['priority'], reverse=True)
    return render(request, "task_05/todo_sorted.html", {"tasks": sorted_tasks})
from django.shortcuts import render

