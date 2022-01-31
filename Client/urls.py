from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('error/',views.error,name="error"),
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('get/',views.get,name='get'),
    path('monitor/',views.monitor,name="monitor"),
]
