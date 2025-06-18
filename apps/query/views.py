from django.shortcuts import render
from apps.structured.models import StructuredRecord
from apps.unstructured.models import UnstructuredDocument
from django.db.models import Q


def structured_filter_view(request):
    """
    Filters structured records using dynamic query params.
    Supports exact or numeric filtering via ?field=net_income&op=gt&value=5000
    """
    field = request.GET.get("field")
    op = request.GET.get("op", "exact")  # eq, gt, gte, lt, lte
    value = request.GET.get("value")

    records = StructuredRecord.objects.filter(is_latest=True)

    if field and value:
        try:
            lookup = f"data__{field}__{op}"
            records = records.filter(**{lookup: value})
        except Exception:
            records = StructuredRecord.objects.none()

    return render(request, "query/structured_results.html", {
        "records": records,
        "field": field,
        "op": op,
        "value": value
    })


def unstructured_search_view(request):
    """
    Performs keyword search on flattened unstructured text.
    """
    keyword = request.GET.get("q", "")
    documents = []

    if keyword:
        documents = UnstructuredDocument.objects.filter(
            is_latest=True,
            text__icontains=keyword
        )

    return render(request, "query/unstructured_results.html", {
        "documents": documents,
        "keyword": keyword
    })


def record_history_view(request, record_id):
    """
    Shows all historical versions of a given structured record ID.
    """
    versions = StructuredRecord.objects.filter(record_id=record_id).order_by("-version")

    return render(request, "query/record_history.html", {
        "versions": versions,
        "record_id": record_id
    })
