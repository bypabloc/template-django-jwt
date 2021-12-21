from django.urls import path
from ..controllers.UserController import list

urlpatterns = [
    path('list', list, name='list'),
]