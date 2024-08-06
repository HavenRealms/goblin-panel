from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from .models import *

# Create your views here.
class AdminDashboard404View(LoginRequiredMixin, TemplateView):
    template_name = "serveradmin/404.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = '404'
        context['version'] = settings.VERSION
        context["user"] = self.request.user
        return context

class AdminDashboardView(LoginRequiredMixin, TemplateView):
    template_name = "serveradmin/dashboard.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Dashboard'
        context['version'] = settings.VERSION
        context["user"] = self.request.user
        return context

class AdminLocationsView(LoginRequiredMixin, TemplateView):
    template_name = "serveradmin/locations.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Locations"
        context["version"] = settings.VERSION
        context["user"] = self.request.user
        context["locations"] = Location.objects.all()
        return context

class AdminLocationDetailView(LoginRequiredMixin, TemplateView):
    template_name = "serveradmin/location-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Locations"
        context["version"] = settings.VERSION
        context["user"] = self.request.user
        context["location"] = get_object_or_404(Location, id=self.kwargs["id"])
        return context