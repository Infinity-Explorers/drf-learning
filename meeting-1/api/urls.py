from django.urls import path
from .import views


urlpatterns = [
    path("hello/", views.hello_api),
    path("by/", views.good_by_api),
]