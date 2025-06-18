from django import forms
from apps.schemas.models import SchemaDefinition
from apps.common.validators import validate_record_against_schema
from .services import StructuredRecordService


class StructuredRecordForm(forms.Form):
    """
    Django form to upload structured data validated against a selected schema.
    """

    record_id = forms.UUIDField(required=False, help_text="Leave blank to create a new record")
    schema = forms.ModelChoiceField(queryset=SchemaDefinition.objects.all())
    data = forms.JSONField(help_text="Structured data as JSON")

    def clean_data(self):
        """
        Validates the data field using the selected schema.
        """
        schema = self.cleaned_data.get("schema")
        data = self.cleaned_data.get("data")

        if schema and data:
            validate_record_against_schema(data, schema.schema)

        return data

    def save(self):
        """
        Delegates record ingestion to the service layer.
        """
        schema = self.cleaned_data["schema"]
        data = self.cleaned_data["data"]
        record_id = self.cleaned_data.get("record_id")

        service = StructuredRecordService(schema=schema)
        return service.ingest_new_record(data, record_id)
