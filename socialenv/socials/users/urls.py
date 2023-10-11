from django.contrib import admin
from django.urls import path, include

from .views import  UserView

urlpatterns = [
    path('', UserView.as_view()),
    path('create/', UserView.as_view()),
    path('update/', UserView.as_view()),
    path('delete/', UserView.as_view())
]
