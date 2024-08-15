from django.db import models

# Create your models here.
class Location(models.Model):
    short_code = models.CharField(max_length=5)
    description = models.CharField(max_length=255)

    def __str__(self):
        return "(" + self.short_code + ") " + self.description


import uuid
from django.db import models

class Node(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    location = models.ForeignKey('Location', on_delete=models.CASCADE, related_name="nodes")
    fqdn = models.CharField(max_length=255)
    ssl = models.BooleanField(default=True)
    proxy = models.BooleanField(default=False)
    memory = models.PositiveIntegerField(help_text="Memory in MB")
    memory_overallocate = models.PositiveIntegerField(default=0, help_text="Memory over-allocation percentage")
    disk = models.PositiveIntegerField(help_text="Disk space in MB")
    disk_overallocate = models.PositiveIntegerField(default=0, help_text="Disk space over-allocation percentage")
    daemon_token = models.CharField(max_length=255, unique=True, blank=True)
    max_upload_size = models.PositiveIntegerField(default=100, help_text="Max upload size in MB")
    public = models.BooleanField(default=False, help_text="Whether the node is publicly visible")

    def save(self, *args, **kwargs):
        if not self.daemon_token:
            self.daemon_token = uuid.uuid4().hex
        super().save(*args, **kwargs)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Allocation(models.Model):
    node = models.ForeignKey(Node, on_delete=models.CASCADE)
    address = models.CharField(max_length=128)
    alias = models.CharField(max_length=256)
    port = models.PositiveIntegerField()


class Database(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255, blank=True, null=True)  # Consider using Django's encrypted fields for passwords
    host = models.CharField(max_length=255)
    port = models.PositiveIntegerField()
    node = models.ForeignKey(Node, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name} on {self.node.name}"

class Hoarde(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    uuid = models.CharField(max_length=32, unique=True)
    author = models.EmailField()

    def __str__(self):
        return f"{self.name} ({self.author})"