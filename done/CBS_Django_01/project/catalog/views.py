from django.http import HttpResponse, HttpRequest

def catalog(request: HttpRequest):
    return HttpResponse('<h1>THIS CATALOG PAGE</h1>')

def product(request: HttpRequest):
    return HttpResponse('<h1>THIS PRODUCT PAGE</h1>')

def info(request: HttpRequest):
    return HttpResponse('<h1>CATALOG INFO PAGE</h1>')