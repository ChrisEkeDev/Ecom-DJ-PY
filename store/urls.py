from django.urls import include, path
from django.contrib import admin;

urlpatterns = [
    path("store/", include('store.urls')),
    path("admin/", admin.site.urls)
]
