import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import os
from core.tool_registry import get_tool_registry
from core.prompt_builder import build_system_prompt
from core.llm_client import call_llm_for_tool_call
from core.parser import parse_tool_call
from core.executor import execute_tool_call

def run(query: str):
    os.environ["LLM_PROVIDER"] = "dummy"
    registry = get_tool_registry()
    system_prompt = build_system_prompt(registry)
    llm_response = call_llm_for_tool_call(system_prompt, query)
    fn, params = parse_tool_call(llm_response)
    result = execute_tool_call(fn, params, registry)
    print(f"Q: {query}\nTool call: {fn} {params}\nResult: {result}\n")

if __name__ == "__main__":
    run("to_uppercase 'hello world'")
    run("to_lower 'OpenAI Copilot'")
    run("length 'OpenAI Copilot'")
    run("concat 'foo' and 'bar'")
    run("concat 'foo' and 'bar' with sep '-'")
