from django.db import models
from apps.schemas.models import SchemaDefinition
import uuid


class StructuredRecord(models.Model):
    """
    Stores structured data entries that follow a defined schema.
    Supports versioning (SCD Type 2): each update creates a new version.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    record_id = models.UUIDField(help_text="Logical group for record versions")
    schema = models.ForeignKey(SchemaDefinition, on_delete=models.PROTECT, related_name="structured_records")
    data = models.JSONField(help_text="Actual structured record (validated)")
    version = models.PositiveIntegerField(default=1)
    is_latest = models.BooleanField(default=True)

    valid_from = models.DateTimeField(auto_now_add=True)
    valid_to = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ("record_id", "version")
        ordering = ["-valid_from"]

    def __str__(self):
        return f"Record {self.record_id} (v{self.version})"
