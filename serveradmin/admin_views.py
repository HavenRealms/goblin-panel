from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class AdminDashboardView(LoginRequiredMixin, TemplateView):
    template_name = "admin/dashboard.html"