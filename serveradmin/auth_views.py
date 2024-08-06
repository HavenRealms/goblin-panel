from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from contrib.auth.mixins import LoggedOutRequiredMixin

# Create your views here.
class AuthLoginView(LoggedOutRequiredMixin, TemplateView):
    template_name = "auth/login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Admin Login'
        return context

class AuthRegisterView(LoggedOutRequiredMixin, TemplateView):
    template_name = "auth/register.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Registration'
        return context
