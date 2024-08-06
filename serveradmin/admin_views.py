from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings

# Create your views here.
class AdminDashboardView(LoginRequiredMixin, TemplateView):
    template_name = "serveradmin/dashboard.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Dashboard'
        context['version'] = settings.VERSION
        context["user"] = self.request.user
        return context