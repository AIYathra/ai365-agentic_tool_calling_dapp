def to_upper(text: str) -> str:
    """Convert the given text to uppercase."""
    return text.upper()


def to_lower(text: str) -> str:
    """Convert the given text to lowercase."""
    return text.lower()


def concat(a: str, b: str, separator: str = " ") -> str:
    """Concatenate two strings with an optional separator."""
    return f"{a}{separator}{b}"
