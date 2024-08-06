from django.urls import path
from .auth_views import *
from .admin_views import *

urlpatterns = [
    path('auth/login/', AuthLoginView.as_view(), name="auth-login"),
    path('auth/register/', AuthRegisterView.as_view(), name="auth-register"),
    path('admin/', AdminDashboardView.as_view(), name="admin-dashboard-home"),
]