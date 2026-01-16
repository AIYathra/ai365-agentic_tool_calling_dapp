def plus(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def minus(a: float, b: float) -> float:
    """Return the result of a minus b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the result of a divided by b."""
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b


def power(a: float, b: float) -> float:
    """Return a raised to the power of b."""
    return a ** b


def modulo(a: int, b: int) -> int:
    """Return the remainder when a is divided by b."""
    if b == 0:
        raise ValueError("Modulo by zero is not allowed.")
    return a % b
