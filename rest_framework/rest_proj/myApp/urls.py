from django.urls import path
from myApp import views

urlpatterns = [
    path("hello-world", views.hello_world),
    # 127.0.0.1:8000/hello-world
    path("hello", views.hello),
    # 127.0.0.1:8000/hello
    path("calculator", views.calculator)
]
