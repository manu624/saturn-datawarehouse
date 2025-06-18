from django import forms
from .models import SchemaDefinition
from apps.common.validators import validate_json_schema


class SchemaDefinitionForm(forms.ModelForm):
    """
    Form to create a new SchemaDefinition.
    Validates that the JSON schema is correctly structured.
    """

    class Meta:
        model = SchemaDefinition
        fields = ["name", "schema"]
        widgets = {
            "schema": forms.Textarea(attrs={"rows": 10, "placeholder": '{"fields": {"name": "string"}}'})
        }

    def clean_schema(self):
        schema = self.cleaned_data["schema"]
        validate_json_schema(schema)  # raises ValidationError if invalid
        return schema
