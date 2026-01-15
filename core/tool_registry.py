import inspect
from typing import Callable, Dict

from tools import math_tools, string_tools


def _collect_functions(module) -> Dict[str, Callable]:
    funcs: Dict[str, Callable] = {}
    for name, obj in inspect.getmembers(module, inspect.isfunction):
        if name.startswith("_"):
            continue
        funcs[name] = obj
    return funcs


def get_tool_registry() -> Dict[str, Callable]:
    """
    Collect all public functions from tools modules into a single registry.
    Keys are function names, values are callables.
    """
    registry: Dict[str, Callable] = {}
    registry.update(_collect_functions(math_tools))
    registry.update(_collect_functions(string_tools))
    return registry
