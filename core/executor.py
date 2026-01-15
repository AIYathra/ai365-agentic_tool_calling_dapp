from typing import Any, Callable, Dict


def execute_tool_call(
    function_name: str,
    params: Dict[str, Any],
    registry: Dict[str, Callable],
) -> Any:
    """
    Execute the given function name with parameters using the provided registry.
    """
    if function_name not in registry:
        raise ValueError(f"Unknown function: {function_name}")

    func = registry[function_name]
    return func(**params)
