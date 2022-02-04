from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone
from . import models

def client(request):
    return render(request, 'index.html')

def server(request):
    return render(request, 'server.html')

def get(request):
    user_request = models.Request(method="GET", server=request.POST["server"], header="{}",  body="{}")
    user_request.save()
    return render(request, 'index.html')

def monitor(request):
    requests = models.Request.objects.filter(time=None)
    return JsonResponse({"request":[
        {
            "method":r.method,
            "server":r.server,
            "header":r.header,
            "body":r.body,
            "pk":r.pk,
        } 
        for r in requests
    ]})

def handle(request):
    r = models.Request.objects.get(pk=request.POST["pk"])
    r.time = timezone.now()
    r.save()
    return JsonResponse({"message":"Success : Handled " + r.server})