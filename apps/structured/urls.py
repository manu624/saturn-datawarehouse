from django.urls import path
from .views import ingest_structured_view

app_name = "structured"

urlpatterns = [
    path("ingest/", ingest_structured_view, name="ingest"),
]
