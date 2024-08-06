from django.urls import path
from .auth_views import *
from .admin_views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', AdminDashboardView.as_view(), name="admin-dashboard-home"),
    path('auth/login/', AuthLoginView.as_view(), name="auth-login"),
    path('auth/logout/', auth_views.LogoutView.as_view(), name="auth-logout"),
    path('auth/register/', AuthRegisterView.as_view(), name="auth-register"),
]