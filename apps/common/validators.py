from django.core.exceptions import ValidationError


def validate_json_schema(schema):
    """
    Validates that a schema has a 'fields' dict and optional 'required' list.

    Args:
        schema (dict): schema definition

    Raises:
        ValidationError: if schema structure is invalid
    """
    if not isinstance(schema, dict):
        raise ValidationError("Schema must be a JSON object.")

    if "fields" not in schema:
        raise ValidationError("Schema must contain a 'fields' key.")

    if not isinstance(schema["fields"], dict):
        raise ValidationError("'fields' must be a dictionary.")

    for field, field_type in schema["fields"].items():
        if field_type not in ("string", "integer", "float", "boolean"):
            raise ValidationError(f"Unsupported type '{field_type}' for field '{field}'.")

    if "required" in schema and not isinstance(schema["required"], list):
        raise ValidationError("'required' must be a list if provided.")



def validate_record_against_schema(data: dict, schema: dict):
    """
    Validates a single structured record against the provided schema definition.
    """
    if "fields" not in schema:
        raise ValidationError("Invalid schema. Missing 'fields' definition.")

    for field, field_type in schema["fields"].items():
        if field not in data:
            continue  # could be optional

        value = data[field]
        if field_type == "string" and not isinstance(value, str):
            raise ValidationError(f"'{field}' must be a string.")
        elif field_type == "integer" and not isinstance(value, int):
            raise ValidationError(f"'{field}' must be an integer.")
        elif field_type == "float" and not isinstance(value, (float, int)):
            raise ValidationError(f"'{field}' must be a float.")
        elif field_type == "boolean" and not isinstance(value, bool):
            raise ValidationError(f"'{field}' must be a boolean.")

    if "required" in schema:
        for field in schema["required"]:
            if field not in data:
                raise ValidationError(f"'{field}' is required.")
