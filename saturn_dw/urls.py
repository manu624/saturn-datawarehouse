"""
URL configuration for saturn_dw project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.dashboard.urls", namespace="dashboard")),
    path("schemas/", include("apps.schemas.urls", namespace="schemas")),
    path("structured/", include("apps.structured.urls", namespace="structured")),
    path("unstructured/", include("apps.unstructured.urls", namespace="unstructured")),
    path("query/", include("apps.query.urls", namespace="query")),
]

