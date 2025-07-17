from django.http import HttpResponse, HttpRequest

def contact(request: HttpRequest):
    return HttpResponse('<h1>CONTACT MAIN PAGE</h1>')

def contact_help(request: HttpRequest):
    return HttpResponse('<h1>CONTACT HELP PAGE</h1>')
