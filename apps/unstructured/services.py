import uuid
from datetime import datetime
from django.db import transaction
from .models import UnstructuredDocument


class UnstructuredDocumentService:
    """
    Service class for managing unstructured document versioning and ingestion.
    """

    @transaction.atomic
    def ingest_new_document(self, content: dict, text: str, doc_id: uuid.UUID = None) -> UnstructuredDocument:
        """
        Ingest a new versioned unstructured document.

        Args:
            content (dict): full original JSON content
            text (str): flattened searchable text
            doc_id (uuid.UUID, optional): reuse existing doc_id for versioning

        Returns:
            UnstructuredDocument: new document instance
        """
        if doc_id is None:
            doc_id = uuid.uuid4()
            version = 1
        else:
            latest = UnstructuredDocument.objects.filter(doc_id=doc_id, is_latest=True).first()
            if latest:
                latest.is_latest = False
                latest.valid_to = datetime.utcnow()
                latest.save(update_fields=["is_latest", "valid_to"])
                version = latest.version + 1
            else:
                version = 1

        return UnstructuredDocument.objects.create(
            doc_id=doc_id,
            content=content,
            text=text,
            version=version,
            is_latest=True
        )
