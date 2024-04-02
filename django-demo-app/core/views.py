from django.shortcuts import render
from django.http import HttpResponse

def sayHello(request):

    context = {"name":"Kapil"}
    return render(request, "index.html", context)