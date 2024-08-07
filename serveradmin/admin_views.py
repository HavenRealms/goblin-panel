from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, View
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect
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
        context["location"] = get_object_or_404(Location, id=self.kwargs["id"])
        context["page_title"] = "Location #" + str(context["location"].id)
        context["version"] = settings.VERSION
        context["user"] = self.request.user
        return context

class AdminLocationEditView(LoginRequiredMixin, TemplateView):
    template_name = "serveradmin/location-edit.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["location"] = get_object_or_404(Location, id=self.kwargs["id"])
        context["page_title"] = "Editinng Location #" + str(context["location"].id)
        context["version"] = settings.VERSION
        context["user"] = self.request.user
        return context
    def post(self, request, *args, **kwargs):
        # Get the POST data
        id = request.POST.get('id')
        short_code = request.POST.get('short_code')
        description = request.POST.get('description')

        # Check if required data is present
        if not id or not short_code or not description:
            return HttpResponseBadRequest("Missing required fields.")

        if id == "" or short_code == "" or description == "":
            redirect("admin-locations")

        # Create and save the new Location instance
        location = Location.objects.get(pk=id)
        location.short_code = short_code
        location.description = description
        location.save()

        # Redirect to the admin locations page
        return redirect('admin-locations')

class AdminLocationCreateView(View):
    def post(self, request, *args, **kwargs):
        # Get the POST data
        short_code = request.POST.get('short_code')
        description = request.POST.get('description')

        # Check if required data is present
        if not short_code or not description:
            return HttpResponseBadRequest("Missing required fields.")

        if short_code == "" or description == "":
            redirect("admin-locations")

        # Create and save the new Location instance
        Location.objects.create(short_code=short_code, description=description)

        # Redirect to the admin locations page
        return redirect('admin-locations')