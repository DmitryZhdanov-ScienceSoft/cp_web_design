from django.contrib import admin
from django.urls import path, include
from .views import health_check

urlpatterns = [
    path('admin/', admin.site.urls),
    path('brief/', include('website_brief.urls')),
    path('health/', health_check, name='health_check'),
]
