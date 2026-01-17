import datetime

def current_year() -> int:
    """Return the current year."""
    return datetime.datetime.now().year


def days_between(date1: str, date2: str) -> int:
    """Return number of days between two YYYY-MM-DD dates."""
    d1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
    d2 = datetime.datetime.strptime(date2, "%Y-%m-%d")
    return abs((d2 - d1).days)