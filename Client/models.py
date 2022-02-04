from email.policy import default
from django.db import models
from django.forms import BooleanField
from django.utils import timezone

#TODO: Have requests say server as a string without manytomany. just like with email client
class Server(models.Model):
    name = models.CharField(max_length=200, default='default')

class Request(models.Model):
    method = models.CharField(max_length=100)
    server = models.CharField(max_length=100)
    header = models.CharField(max_length=10000, default="{}")
    body = models.CharField(max_length=10000, default="{}")
    time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "GET " + self.server + " HEADER:" + self.header + " BODY:" + self.body 

    def handle(self):
        self.handled = True