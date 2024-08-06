from django.urls import path
from .auth_views import *
from .admin_views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', AdminDashboardView.as_view(), name="admin-dashboard-home"),
    path('admin/locations/', AdminLocationsView.as_view(), name="admin-locations"),
    path('admin/locations/view/<int:id>/', AdminLocationDetailView.as_view(), name='admin-location-detail'),
    path('admin/locations/new/', AdminLocationCreateView.as_view(), name='admin-location-create'),

    path('auth/login/', AuthLoginView.as_view(), name="auth-login"),
    path('auth/logout/', auth_views.LogoutView.as_view(), name="auth-logout"),
    path('auth/register/', AuthRegisterView.as_view(), name="auth-register"),
]