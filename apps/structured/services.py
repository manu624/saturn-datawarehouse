import uuid
from datetime import datetime
from django.db import transaction
from .models import StructuredRecord
from apps.schemas.models import SchemaDefinition


class StructuredRecordService:
    """
    Service layer for handling structured record ingestion and version control.
    """

    def __init__(self, schema: SchemaDefinition):
        self.schema = schema

    @transaction.atomic
    def ingest_new_record(self, data: dict, record_id: uuid.UUID = None) -> StructuredRecord:
        """
        Creates or updates a versioned record within a record group.

        Args:
            data (dict): validated structured data
            record_id (UUID): optional, to update existing record group

        Returns:
            StructuredRecord: the new versioned record instance
        """
        if record_id is None:
            record_id = uuid.uuid4()
            version = 1
        else:
            latest = StructuredRecord.objects.filter(
                record_id=record_id,
                is_latest=True
            ).first()

            if latest:
                latest.is_latest = False
                latest.valid_to = datetime.utcnow()
                latest.save(update_fields=["is_latest", "valid_to"])
                version = latest.version + 1
            else:
                version = 1

        return StructuredRecord.objects.create(
            record_id=record_id,
            schema=self.schema,
            data=data,
            version=version,
            is_latest=True
        )
