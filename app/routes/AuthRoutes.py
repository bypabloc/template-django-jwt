from django.urls import path
from ..controllers.AuthController import signUp

urlpatterns = [
    path('sign_up', signUp, name='signUp'),
]