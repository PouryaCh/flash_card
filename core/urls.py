
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('card/', include('card.urls'),),
    path('users/', include('Users.urls')),


]
