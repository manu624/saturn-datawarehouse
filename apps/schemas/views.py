from django.shortcuts import render, redirect
from .forms import SchemaDefinitionForm


def create_schema_view(request):
    """
    Renders and handles the form to create a new SchemaDefinition.
    """
    if request.method == "POST":
        form = SchemaDefinitionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("schemas:create")  # or dashboard
    else:
        form = SchemaDefinitionForm()

    return render(request, "schemas/create_schema.html", {"form": form})
