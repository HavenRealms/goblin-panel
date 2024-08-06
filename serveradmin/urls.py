from django.urls import path
from .views import *

urlpatterns = [
    path('auth/login/', AuthLoginView.as_view()),
    path('auth/register/', AuthRegisterView.as_view()),
]