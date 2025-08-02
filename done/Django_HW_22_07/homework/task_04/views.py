from django.http import HttpResponse, JsonResponse, FileResponse
from django.shortcuts import render
import os


def text_view(request):
    return HttpResponse("Це текстова відповідь", content_type="text/plain; charset=utf-8")


def html_view(request):
    return HttpResponse("<h1>Це HTML-відповідь</h1><p>Привіт з Django!</p>", content_type="text/html; charset=utf-8")


def json_view(request):
    data = {
        "message": "Це JSON-відповідь",
        "status": "success",
        "items": [1, 2, 3]
    }
    return JsonResponse(data, json_dumps_params={"ensure_ascii": False})


def file_view(request):
    filepath = os.path.join(os.path.dirname(__file__), "my_file.txt")

    if not os.path.exists(filepath):
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("Це вміст файлу з task_04.")

    return FileResponse(open(filepath, "rb"), as_attachment=True, filename="my_file.txt")
