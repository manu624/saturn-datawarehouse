from django.shortcuts import render, redirect
from .forms import StructuredRecordForm


def ingest_structured_view(request):
    """
    Renders and processes the form to ingest a structured record.
    """
    if request.method == "POST":
        form = StructuredRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("structured:ingest")  # Optional: redirect to confirmation
    else:
        form = StructuredRecordForm()

    return render(request, "structured/ingest.html", {"form": form})
