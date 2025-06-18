from django.shortcuts import render, redirect
from .forms import UnstructuredDocumentForm


def ingest_unstructured_view(request):
    """
    Renders and processes the form for unstructured document ingestion.
    """
    if request.method == "POST":
        form = UnstructuredDocumentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("unstructured:ingest")
    else:
        form = UnstructuredDocumentForm()

    return render(request, "unstructured/ingest.html", {"form": form})
