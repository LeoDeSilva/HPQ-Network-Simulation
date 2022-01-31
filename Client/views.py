from django.http import JsonResponse
from django.shortcuts import render
from . import models

def dashboard(request):
    return render(request, 'index.html')

def error(request):
    return render(request, 'error.html')

def register(request):
    print("REGISTER", request)
    return render(request,'index.html')

def login(request):
    print("LOGIN")
    return render(request, 'index.html')

def get(request):
    user_request = models.Request(method="GET", server=request.POST["server"], header="{}",  body="{}")
    user_request.save()
    print(user_request)
    return render(request, 'index.html')

def monitor(request):
    requests = models.Request.objects.filter()
    for r in requests:
        print("R",r.method)
    return JsonResponse({"request":[
        {
            "method":r.method,
            "server":r.server,
            "header":r.header,
            "body":r.body,
        } 
        for r in requests
    ]})
