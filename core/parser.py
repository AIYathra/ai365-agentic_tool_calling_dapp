import ast
from typing import Any, Dict, Tuple

def parse_tool_call(raw: str) -> Tuple[str, Dict[str, Any]]:
  """
    Parse a tool-call string of the form:

        function_name - {'a': 2, 'b': 8}

    Returns:
        (function_name, params_dict)
  """
  if "-" not in raw:
    raise ValueError(f"Invalid tool call format: {raw}")
  
  fn_part, params_part = raw.split("-", 1)
  fn_name = fn_part.strip()
  
  params_str = params_part.strip()
  try:
    params = ast.literal_eval(params_str)
  except Exception as e:
    raise ValueError(f"Failed to parse parameters: {params_str}") from e
  
  if not isinstance(params, dict):
    raise ValueError(f"Parameters must be a dictionary, got: {type(params)}")
  
  return fn_name, params
    
