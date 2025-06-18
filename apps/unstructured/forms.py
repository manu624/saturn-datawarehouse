from django import forms
from .services import UnstructuredDocumentService


class UnstructuredDocumentForm(forms.Form):
    """
    Django form for submitting unstructured or free-form content.
    """
    doc_id = forms.UUIDField(required=False, help_text="Leave blank to create a new document")
    content = forms.JSONField(help_text="Original nested JSON or document")
    text = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 4}),
        help_text="Flattened version of document for full-text search"
    )

    def save(self):
        doc_id = self.cleaned_data.get("doc_id")
        content = self.cleaned_data["content"]
        text = self.cleaned_data["text"]

        service = UnstructuredDocumentService()
        return service.ingest_new_document(content, text, doc_id)
