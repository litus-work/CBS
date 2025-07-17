from django.http import HttpResponse, HttpRequest

def hello_world(request: HttpRequest):
    return HttpResponse("""
        <p>Hello World!</p>
        <p>Django є одним з найбільших framework на Python</p>
        <hr>
    """)