from typing import Callable, Dict


def build_system_prompt(registry: Dict[str, Callable]) -> str:
    """
    Build a system prompt that lists available tools, their signatures,
    and usage format.
    """
    lines = []
    lines.append("You are a tool-calling assistant.")
    lines.append("You ONLY respond with a single tool call in this format:")
    lines.append("")
    lines.append("    function_name - {'param1': value1, 'param2': value2}")
    lines.append("")
    lines.append("Available tools:")

    for name, func in registry.items():
        doc = (func.__doc__ or "").strip().replace("\n", " ")
        lines.append(f"- {name}: {doc}")

    lines.append("")
    lines.append("Do not explain your reasoning. Just output the tool call.")
    return "\n".join(lines)

