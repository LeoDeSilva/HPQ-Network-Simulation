from django.urls import path
from . import views

urlpatterns = [
    path('',views.client,name='client'),
    path('server/',views.server,name='server'),
    path('get/',views.get,name='get'),
    path('monitor/',views.monitor,name="monitor"),
    path('handle/',views.handle,name='handle'),
]
