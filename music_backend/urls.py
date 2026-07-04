from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # यहाँ admin.py की जगह admin.site.urls होना चाहिए
    path('', include('core.urls')),
]