from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, View
from django.contrib.auth.models import User
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from .models import *
from json import dumps

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

class AdminNodesView(LoginRequiredMixin, TemplateView):
    template_name = "serveradmin/nodes.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Nodes"
        context["version"] = settings.VERSION
        context["user"] = self.request.user
        context["nodes"] = Node.objects.all()
        return context

class AdminNodeDetailView(LoginRequiredMixin, TemplateView):
    template_name = "serveradmin/node-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["node"] = get_object_or_404(Node, id=self.kwargs["id"])
        context["page_title"] = context["node"].name
        context["version"] = settings.VERSION
        context["user"] = self.request.user
        return context

class AdminNodeConfigView(LoginRequiredMixin, TemplateView):
    template_name = "serveradmin/node-detail-config.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["node"] = get_object_or_404(Node, id=self.kwargs["id"])
        context["page_title"] = context["node"].name
        context["version"] = settings.VERSION
        context["user"] = self.request.user
        return context

class AdminNodeSettingsView(LoginRequiredMixin, TemplateView):
    template_name = "serveradmin/node-detail-settings.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["node"] = get_object_or_404(Node, id=self.kwargs["id"])
        context["page_title"] = context["node"].name
        context["version"] = settings.VERSION
        context["locations"] = Location.objects.all()
        context["users"] = User.objects.all()
        context["user"] = self.request.user
        return context
    def post(self, request, *args, **kwargs):
        node = get_object_or_404(Node, id=self.kwargs["id"])
        # Get the POST data
        name = request.POST.get('serverName')
        description = request.POST.get('serverDescription')
        location = request.POST.get("serverLocation")
        address = request.POST.get("serverAddress")
        ssl = request.POST.get("serverSSL")
        proxy = request.POST.get("serverProxy")
        memory = request.POST.get("serverMemory")
        memory_over = request.POST.get("serverMemoryOver")
        disk = request.POST.get("serverDiskSpace")
        disk_over = request.POST.get("serverDiskSpaceOver")
        upload_max = request.POST.get("serverMaxUploadSize")
        visible = request.POST.get("serverVisible")

        # Check if required data is present
        if not name or not location or not address or not ssl or not proxy or not memory or not memory_over or not disk or not disk_over or not upload_max or not visible:
            return HttpResponseBadRequest("Missing required fields: " + dumps(request.POST))

        if name == "" or location == "" or address == "" or memory == "" or memory_over == "" or disk == "" or disk_over == "" or upload_max == "":
            redirect("admin-node-detail", id=node.id)

        # Create and save the new Node instance
        location = Location.objects.get(pk=int(location))
        node.name=name
        node.description=description
        node.location=location
        node.fqdn=address
        node.memory=memory
        node.memory_overallocate=memory_over
        node.disk=disk
        node.disk_overallocate=disk_over
        node.max_upload_size=upload_max
        node.public=visible

        node.save()

        # Redirect to the admin locations page
        return redirect('admin-node-detail', id=node.id)

class AdminNodeAllocationsView(LoginRequiredMixin, TemplateView):
    template_name = "serveradmin/node-detail-allocations.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["node"] = get_object_or_404(Node, id=self.kwargs["id"])
        context["page_title"] = context["node"].name
        context["version"] = settings.VERSION
        context["allocations"] = Allocation.objects.filter(node=context["node"])
        context["user"] = self.request.user
        return context

    def post(self, request, *args, **kwargs):
        node = get_object_or_404(Node, id=self.kwargs["id"])
        allocations = Allocation.objects.filter(node=node)
        for allocation in allocations:
            if "address-" + str(allocation.id) in request.POST and "alias-" + str(allocation.id) in request.POST and "port-" + str(allocation.id) in request.POST:
                allocation.address = request.POST.get("address-" + str(allocation.id))
                allocation.alias = request.POST.get("alias-" + str(allocation.id))
                allocation.port = request.POST.get("port-" + str(allocation.id))
                allocation.save()
        for value in request.POST:
            if value.startswith("delete-"):
                id = int(value.replace("delete-", ""))
                allocation = get_object_or_404(Allocation, id=id)
                allocation.delete()
        if "address-new" in request.POST and "alias-new" in request.POST and "port-new" in request.POST:
            address = request.POST.get("address-new")
            alias = request.POST.get("alias-new")
            port = request.POST.get("port-new")
            if address != "" and alias != "" and port != "":
                Allocation.objects.create(
                    node=node,
                    address=address,
                    alias=alias,
                    port=int(port)
                )
        return redirect("admin-node-allocations", id=node.id)

class AdminNodeCreateView(LoginRequiredMixin, TemplateView):
    template_name = "serveradmin/node-create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Create Node"
        context["version"] = settings.VERSION
        context["locations"] = Location.objects.all()
        context["users"] = User.objects.all()
        context["user"] = self.request.user
        return context
    def post(self, request, *args, **kwargs):
        # Get the POST data
        name = request.POST.get('serverName')
        description = request.POST.get('serverDescription')
        location = request.POST.get("serverLocation")
        address = request.POST.get("serverAddress")
        ssl = request.POST.get("serverSSL")
        proxy = request.POST.get("serverProxy")
        memory = request.POST.get("serverMemory")
        memory_over = request.POST.get("serverMemoryOver")
        disk = request.POST.get("serverDiskSpace")
        disk_over = request.POST.get("serverDiskSpaceOver")
        upload_max = request.POST.get("serverMaxUploadSize")
        visible = request.POST.get("serverVisible")

        # Check if required data is present
        if not name or not location or not address or not ssl or not proxy or not memory or not memory_over or not disk or not disk_over or not upload_max or not visible:
            return HttpResponseBadRequest("Missing required fields: " + dumps(request.POST))

        if name == "" or location == "" or address == "" or memory == "" or memory_over == "" or disk == "" or disk_over == "" or upload_max == "":
            redirect("admin-nodes")

        # Create and save the new Node instance
        location = Location.objects.get(pk=int(location))
        Node.objects.create(
            name=name,
            description=description,
            location=location,
            fqdn=address,
            memory=memory,
            memory_overallocate=memory_over,
            disk=disk,
            disk_overallocate=disk_over,
            max_upload_size=upload_max,
            public=visible
        )

        # Redirect to the admin locations page
        return redirect('admin-nodes')

class AdminDatabasesView(LoginRequiredMixin, TemplateView):
    template_name = "serveradmin/databases.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Databases"
        context["version"] = settings.VERSION
        context["user"] = self.request.user
        context["databases"] = Database.objects.all()
        return context