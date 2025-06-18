from django import forms
from .services import UnstructuredDocumentService


class UnstructuredDocumentForm(forms.Form):
    """
    Django form for submitting unstructured or free-form content.
    """
    doc_id = forms.UUIDField(required=False, help_text="Leave blank to create a new document")
    content = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 6}),
        help_text="Enter free text or valid JSON"
    )

    def save(self):
        doc_id = self.cleaned_data.get("doc_id")
        raw_input = self.cleaned_data["content"]

        service = UnstructuredDocumentService()
        return service.ingest_new_document(raw_input, doc_id)
