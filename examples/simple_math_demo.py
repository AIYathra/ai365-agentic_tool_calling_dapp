import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from core.llm_client import call_llm_for_tool_call
from core.parser import parse_tool_call
from core.executor import execute_tool_call
from core.tool_registry import get_tool_registry
from core.prompt_builder import build_system_prompt


def run_simple_math_demo():
    user_query = "Add 10 and 25, then subtract 3."
    tools = get_tool_registry()
    system_prompt = build_system_prompt(tools)

    print("[User query]")
    print(user_query)
    print("\n[System prompt]")
    print(system_prompt)

    llm_response = call_llm_for_tool_call(system_prompt, user_query)
    print("\n[LLM raw response]")
    print(llm_response)

    fn_name, params = parse_tool_call(llm_response)
    print(f"\n[Parsed tool call] function={fn_name}, params={params}")

    result = execute_tool_call(fn_name, params, tools)
    print(f"\n[Result]\n{result}")


if __name__ == "__main__":
    run_simple_math_demo()
