from django.urls import path
from .auth_views import *
from .admin_views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('auth/login/', AuthLoginView.as_view(), name="auth-login"),
    path('logout/', auth_views.LogoutView.as_view(), name="auth-logout"),
    path('auth/register/', AuthRegisterView.as_view(), name="auth-register"),
    path('admin/', AdminDashboardView.as_view(), name="admin-dashboard-home"),
]