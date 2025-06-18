from django.urls import path
from .views import ingest_unstructured_view

app_name = "unstructured"

urlpatterns = [
    path("ingest/", ingest_unstructured_view, name="ingest"),
]
