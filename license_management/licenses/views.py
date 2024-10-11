from django.http import JsonResponse, HttpResponseBadRequest
from .models import License
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, get_object_or_404


def home(request):
    return render(request, 'home.html')  # Ensure this template exists

def validate_license(request):
    if request.method == 'POST':
        license_key = request.POST.get('key')

        if not license_key:
            return JsonResponse({"error": "License key is required."}, status=400)

        # Use get_object_or_404 to retrieve the license, which handles the DoesNotExist internally
        license = get_object_or_404(License, key=license_key, is_active=True)
        return JsonResponse({'valid': True, 'expiration_date': license.expiration_date})

def usage_statistics(request):
    active_licenses = License.objects.filter(is_active=True).count()
    return render(request, 'admin/usage_statistics.html', {'active_licenses': active_licenses})

def admin_dashboard(request):
    total_licenses = License.objects.count()
    active_licenses = License.objects.filter(is_active=True).count()
    return render(request, 'admin/dashboard.html', {
        'total_licenses': total_licenses,
        'active_licenses': active_licenses,
    })

def revoke_license(request, license_id):
    if request.method == 'POST':
        # Use get_object_or_404 to handle missing licenses
        license = get_object_or_404(License, id=license_id)
        license.is_active = False  # Mark the license as inactive
        license.save()
        return JsonResponse({'success': True})
