from django.contrib import admin
from django.urls import path, include
from api.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Map the root URL to the home view
    path('api/', include('rest_framework.urls')),  # DRF login/logout views
    path('api/transactions/', include('api.urls')),  # Your app's API endpoints
]