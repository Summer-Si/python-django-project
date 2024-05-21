from django.urls import path
from . import views

# map url to our view functions
# URLConf
urlpatterns = [
    path('hello/', views.say_hello)
]