from django.http import HttpResponse

def download_file(request):
    response = HttpResponse("Ось ваш файл", content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="myfile.txt"'
    response.status_code = 227
    return response
