from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class AuthLoginView(TemplateView):
    template_name = "auth/login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Admin Login'
        return context

class AuthRegisterView(TemplateView):
    template_name = "auth/register.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Registration'
        return context