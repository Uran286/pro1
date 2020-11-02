from django.http import HttpResponse

def get_page(request):
    name = "Yra"
    project = "Just page"
    return HttpResponse(name)


