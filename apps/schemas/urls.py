from django.urls import path
from . import views

app_name = "schemas"

urlpatterns = [
    path("create/", views.create_schema_view, name="create"),
]
