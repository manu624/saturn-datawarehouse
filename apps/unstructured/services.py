import uuid
import json
from datetime import datetime
from django.db import transaction
from .models import UnstructuredDocument


def flatten_json(obj):
    if isinstance(obj, dict):
        return " ".join(flatten_json(v) for v in obj.values())
    elif isinstance(obj, list):
        return " ".join(flatten_json(item) for item in obj)
    return str(obj)


def flatten_input(content):
    if isinstance(content, dict):
        return flatten_json(content)
    return str(content)


def try_parse_json(value: str):
    try:
        return json.loads(value)
    except json.JSONDecodeError:
        return value  # keep as plain text


class UnstructuredDocumentService:
    """
    Service class for managing unstructured document versioning and ingestion.
    """

    @transaction.atomic
    def ingest_new_document(self, raw_input: str, doc_id: uuid.UUID = None) -> UnstructuredDocument:
        """
        Ingest a new versioned unstructured document.

        Args:
            content (dict): full original JSON content
            text (str): flattened searchable text
            doc_id (uuid.UUID, optional): reuse existing doc_id for versioning

        Returns:
            UnstructuredDocument: new document instance
        """
        parsed = try_parse_json(raw_input)
        flat_text = flatten_input(parsed)
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
            content=parsed,
            text=flat_text,
            version=version,
            is_latest=True
        )

