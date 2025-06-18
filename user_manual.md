# Saturn Data Warehouse - User Manual

This user manual will guide you through how to use the system, from creating schemas to ingesting data and searching records.

---

## 📋 Table of Contents

1. [System Overview](#system-overview)
2. [How to Define a Schema](#how-to-define-a-schema)
3. [How to Ingest Structured Records](#how-to-ingest-structured-records)
4. [How to Ingest Unstructured Records](#how-to-ingest-unstructured-records)
5. [View and Manage Datasets](#view-and-manage-datasets)
6. [Search Structured Records](#search-structured-records)
7. [Search Unstructured Records](#search-unstructured-records)
8. [Track Version History](#track-version-history)

---

## 🔧 System Overview

This system allows users to define schemas for structured data, ingest structured or unstructured records, and run queries or search across them. All records are versioned and changes are tracked historically.

Navigate to: `https://saturn-datawarehouse.onrender.com/` to access the main dashboard.

 **Note:** The first time you load the site, it may take 10–20 seconds for the dashboard to appear. This delay is normal due to initial setup and cold start processes.

---

## 🧱 How to Define a Schema

1. Go to **"Define New Schema"** from the dashboard.
2. Provide a unique schema name.
3. Enter your schema JSON in the following format:

```json
{
  "fields": {
    "name": "string",
    "age": "integer",
    "net_income": "float",
    "is_active": "boolean"
  },
  "required": ["name", "net_income"]
}
```

4. Click **Save Schema**.

Supported field types: `string`, `integer`, `float`, `boolean`

---

## 📥 How to Ingest Structured Records

1. Go to **"Ingest Structured Record"**.
2. Select an existing schema.
3. Paste your record JSON. Example:

```json
{
  "name": "Alice",
  "age": 30,
  "net_income": 55000.5,
  "is_active": true
}
```

4. Submit the form. If the record is valid per the schema, it is saved and versioned.

---

## 🧾 How to Ingest Unstructured Records

1. Go to **"Ingest Unstructured Document"**.
2. Paste the original `content` as JSON or Free Text. Example:
```json
{
  "goal": "Save for a new house within 2 years",
  "notes": "Customer plans to invest in mutual funds."
}
```
3. Click submit to ingest the record.

---


## 🔍 Search Structured Records

1. Click **"Query Structured Data"**.
2. Use the form to filter records:
   - `field`: the field name in your schema (e.g. `net_income`)
   - `operator`: exact, gt, lt (e.g. `gt` for greater than)
   - `value`: a value to filter by (e.g. `50000`)
3. Submit to view matching records.

---

## 🧠 Search Unstructured Records

1. Click **"Search Unstructured Text"**.
2. Enter a keyword (e.g., `mutual funds`).
3. Submit the form to see all unstructured records containing that keyword.

---

## 📜 Track Version History

1. On the structured query results page, click the **"History"** link next to any record.
2. You’ll see all previous versions of that record, including timestamps.

---

For any technical setup or system design details, refer to the `README.md` file.

---
