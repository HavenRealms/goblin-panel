from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class AuthLoginView(TemplateView):
    template_name = "auth/login.html"

class AuthRegisterView(TemplateView):
    template_name = "auth/register.html"