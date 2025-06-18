# Saturn Data Warehouse Assignment - Backend System

## 🚀 Overview

This is a prototype for a scalable data warehouse system built using Django. It supports ingestion of both structured and unstructured data, schema-based validation, versioning, and full-text search capabilities. The solution provides a simple Python-based UI (no JS frontend) for interacting with the platform.

---

## 🧱 Design Approach

### Modular App Structure

The project is organized into modular Django apps, each responsible for a specific domain:

- **schemas/**: Define and validate reusable structured schemas.
- **datasets/**: Manage logical datasets linked to schemas.
- **structured/**: Ingest and store versioned structured records.
- **unstructured/**: Handle unstructured/semi-structured text data with versioning.
- **dashboard/**: Central navigation hub for user actions.
- **query/**: Allow filtering of structured data and full-text search over unstructured data.
- **common/**: Shared validators and utilities.

### Key Architectural Patterns

- Uses **JSONField** for flexible storage of structured and unstructured records.
- Applies **SOLID principles**, with clear separation of form/view/service/model layers.
- Follows **SCD Type-2** versioning (new row per update, with valid\_from/valid\_to).
- Clean UI built using **Django templates** and forms.

---

## 📌 Assumptions Made

1. **Schema-Driven Ingestion**: Structured records are validated against user-defined schemas before being accepted.
2. **Versioning**: Every update to a record creates a new version. Previous versions are retained.
3. **Text Flattening**: Users provide flattened text when submitting unstructured documents. (Could be auto-flattened later.)
4. **Search & Filters**: Queries are limited to basic filtering via URL params and basic full-text `icontains` matching.
5. **Minimal Auth**: No authentication or user-level scoping implemented.
6. **Flat storage**: Structured/unstructured records are not currently tied back to `Dataset`, but that could easily be added.

---

## 🛠 How to Run

### 1. Clone & Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Setup Database

```bash
python manage.py migrate
```

### 3. Run Server

```bash
python manage.py runserver
```

### 4. Access the Dashboard

Visit: `http://localhost:8000/`

### 5. Admin Panel (Optional)

```bash
python manage.py createsuperuser
```

Then visit: `http://localhost:8000/admin/`

---

## 🧠 How Change History Is Tracked

### Structured Records

- Each logical record has a `record_id`.
- Each update creates a new row with incremented `version`.
- Fields: `valid_from`, `valid_to`, `is_latest`

### Unstructured Records

- Each document has a `doc_id`.
- Each new version updates the prior one to `is_latest=False`.
- Supports storing and searching by versioned text.

### Example:

```
Record ID: abc-123
- v1: net_income=5000 (2023-01 to 2023-03)
- v2: net_income=5500 (2023-03 to now)
```

---

## 🔭 Production Considerations

| Area                      | Recommendation                                     |
| ------------------------- | -------------------------------------------------- |
| **Validation**            | Replace manual checks with JSON Schema or Pydantic |
| **Text Flattening**       | Auto-flatten nested JSON for unstructured ingest   |
| **Full-Text Search**      | Use PostgreSQL `SearchVector` or Elasticsearch     |
| **Indexing**              | Add GIN indexes on JSONB/text fields               |
| **Auth & Access Control** | Add user accounts, dataset scoping                 |
| **Query Builder**         | Build an advanced query UI layer                   |
| **Data Lineage**          | Track source system, upload origin, tags           |
| **Linking to Dataset**    | Associate all records with a `dataset_id`          |

---

## ✅ Conclusion

This system demonstrates a production-inspired backend architecture that supports flexible data ingestion, validation, history tracking, and querying. It's extensible, testable, and scalable to real-world use cases with minor enhancements.

---

Built with ❤️ by [Your Name] for the Saturn assignment.

