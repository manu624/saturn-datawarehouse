from django.db import models
import uuid


class UnstructuredDocument(models.Model):
    """
    Represents a versioned document containing unstructured or semi-structured data.

    Fields:
        - content: Original JSON (can be nested)
        - text: Flattened version of content for full-text search
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    doc_id = models.UUIDField(help_text="Groups versions of the same document")
    content = models.JSONField()
    text = models.TextField(help_text="Flattened content for search")
    version = models.PositiveIntegerField(default=1)
    is_latest = models.BooleanField(default=True)

    valid_from = models.DateTimeField(auto_now_add=True)
    valid_to = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ("doc_id", "version")
        indexes = [
            models.Index(fields=["is_latest"]),
            models.Index(fields=["text"], name="text_search_idx")
        ]
        ordering = ["-valid_from"]

    def __str__(self):
        return f"Document {self.doc_id} (v{self.version})"
