from django.urls import path
from .views import Hello, Desserialization

urlpatterns = [
    path("",name='hello_api',view=Hello.as_view()),
    path("desserialization/",name='desserialization_api',view=Desserialization.as_view()),
]