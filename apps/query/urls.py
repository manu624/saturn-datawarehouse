from django.urls import path
from .views import (
    structured_filter_view,
    unstructured_search_view,
    record_history_view,
)

app_name = "query"

urlpatterns = [
    path("structured/", structured_filter_view, name="structured_search"),
    path("unstructured/", unstructured_search_view, name="unstructured_search"),
    path("history/<uuid:record_id>/", record_history_view, name="record_history"),
]
