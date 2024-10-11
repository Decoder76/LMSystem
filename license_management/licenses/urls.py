from django.urls import path
from .views import validate_license, usage_statistics, revoke_license, admin_dashboard

urlpatterns = [
    path('validate/', validate_license, name='validate_license'),
    path('usage/', usage_statistics, name='usage_statistics'),
    path('revoke/<int:license_id>/', revoke_license, name='revoke_license'),  # For revoking licenses
    path('admin/dashboard/', admin_dashboard, name='admin_dashboard'),  # Admin dashboard route
]
