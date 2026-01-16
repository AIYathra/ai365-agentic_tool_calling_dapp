import os
import re
from typing import Optional

from groq import Groq


def _get_groq_client() -> Groq:
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("GROQ_API_KEY environment variable is not set.")
    return Groq(api_key=api_key)


def call_llm_for_tool_call(system_prompt: str, user_query: str) -> str:
    """
    Call an LLM to produce a tool-call string.

    Expected output format (example):
        power - {'a': 2, 'b': 8}
    """
    provider = os.getenv("LLM_PROVIDER", "groq").lower()

    if provider == "groq":
        client = _get_groq_client()
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_query},
            ],
            temperature=0,
        )
        content = response.choices[0].message.content.strip()
        return content
    
    if provider == "dummy":
        # Simple heuristic demo: if 'modulo' in query, call modulo, else power.
        # text = user_query.lower()
        # if "modulo" in text or "remainder" in text:
        
        text = user_query.strip()

        # string_tools: to_uppercase '...'
        m = re.match(r"(?i)to_uppercase\s+'(.+)'", text)
        if m:
            return f"to_upper - {{'text': '{m.group(1)}'}}"

        # string_tools: to_lower '...'
        m = re.match(r"(?i)to_lower\s+'(.+)'", text)
        if m:
            return f"to_lower - {{'text': '{m.group(1)}'}}"

        # string_tools: length '...'
        m = re.match(r"(?i)length\s+'(.+)'", text)
        if m:
            return f"length - {{'text': '{m.group(1)}'}}"

        # string_tools: concat 'a' and 'b' [with sep '...']
        m = re.match(r"(?i)concat\s+'(.+)'\s+and\s+'(.+?)'(?:\s+with\s+sep\s+'(.*)')?$", text)
        if m:
            a, b, sep = m.group(1), m.group(2), (m.group(3) or "")
            return f"concat - {{'a': '{a}', 'b': '{b}', 'separator': '{sep}'}}"

        # math_tools: modulo vs power as before
        low = text.lower()
        if "modulo" in low or "remainder" in low:
            return "modulo - {'a': 1000, 'b': 7}"
        else:
            return "power - {'a': 2, 'b': 8}"
    

    raise NotImplementedError(
        f"Unknown LLM_PROVIDER: {provider}. Use 'dummy' or 'groq'."
    )

