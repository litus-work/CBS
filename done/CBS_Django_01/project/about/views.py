from django.http import HttpResponse, HttpRequest

def about(request: HttpRequest):
    return HttpResponse('<h1>ABOUT MAIN PAGE</h1>')

def about_team(request: HttpRequest):
    return HttpResponse('<h1>ABOUT TEAM PAGE</h1>')
