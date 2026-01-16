from typing import Union

Number = Union[int, float]

def plus(a: Number, b: Number) -> Number:
    """Return a + b."""
    return a + b

def minus(a: Number, b: Number) -> Number:
    """Return a - b."""
    return a - b

def multiply(a: Number, b: Number) -> Number:
    """Return a * b."""
    return a * b

def divide(a: Number, b: Number) -> float:
    """Return a / b. Raises ValueError if b == 0."""
    if b == 0:
        raise ValueError("Division by zero")
    return a / b

def power(a: Number, b: Number) -> Number:
    """Return a ** b."""
    return a ** b

def modulo(a: int, b: int) -> int:
    """Return a % b. Raises ValueError if b == 0."""
    if b == 0:
        raise ValueError("Modulo by zero")
    return a % b
