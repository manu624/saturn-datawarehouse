from django.db import models
import uuid


class SchemaDefinition(models.Model):
    """
    Stores user-defined reusable schemas for structured data ingestion.
    Example:
        {
            "fields": {
                "name": "string",
                "age": "integer",
                "net_income": "float"
            },
            "required": ["name", "age"]
        }
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    schema = models.JSONField(help_text="JSON schema definition for the dataset")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Schema Definition"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Schema: {self.name}"
