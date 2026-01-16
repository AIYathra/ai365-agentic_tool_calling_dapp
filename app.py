import sys

from core.llm_client import call_llm_for_tool_call
from core.parser import parse_tool_call
from core.executor import execute_tool_call
from core.tool_registry import get_tool_registry
from core.prompt_builder import build_system_prompt


def main():
    # 1. Accept user input (CLI or interactive)
    if len(sys.argv) > 1:
        user_query = " ".join(sys.argv[1:])
    else:
        user_query = input("Enter your query: ")

    # 2. Load available tools
    tools = get_tool_registry()

    # 3. Build system prompt dynamically
    system_prompt = build_system_prompt(tools)

    # 4. Ask LLM to produce a tool-call string
    llm_response = call_llm_for_tool_call(system_prompt, user_query)
    print(f"\n[LLM raw response]\n{llm_response}\n")

    # 5. Parse the tool-call
    fn_name, params = parse_tool_call(llm_response)
    print(f"[Parsed tool call] function={fn_name}, params={params}")

    # 6. Execute the tool
    result = execute_tool_call(fn_name, params, tools)

    # 7. Return result to user
    print(f"\n[Result]\n{result}")


if __name__ == "__main__":
    main()
