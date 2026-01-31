SUPPORTED_OPERATIONS=["add","subtract","multiply","divide"]


def validate_operation(operation: str) :
    if operation not in SUPPORTED_OPERATIONS:
        raise ValueError(f"Unsupported operation: {operation}")