import os
from typing import Optional


def call_llm_for_tool_call(system_prompt: str, user_query: str) -> str:
    """
    Call an LLM to produce a tool-call string.

    Expected output format (example):
        power - {'a': 2, 'b': 8}

    For now, this is a placeholder should replace with
    a real LLM call (Groq, OpenAI, etc.).
    """
    provider = os.getenv("LLM_PROVIDER", "dummy").lower()

    if provider == "dummy":
        # Simple heuristic demo: if 'modulo' in query, call modulo, else power.
        text = user_query.lower()
        if "modulo" in text or "remainder" in text:
            return "modulo - {'a': 1000, 'b': 7}"
        else:
            return "power - {'a': 2, 'b': 8}"

    # Example skeleton for a real client (pseudo-code):
    #
    # from groq import Groq
    # client = Groq(api_key=os.environ["GROQ_API_KEY"])
    # response = client.chat.completions.create(
    #     model="llama-3.1-8b-instant",
    #     messages=[
    #         {"role": "system", "content": system_prompt},
    #         {"role": "user", "content": user_query},
    #     ],
    #     temperature=0,
    # )
    # return response.choices[0].message.content.strip()
    #
    # Or adapt for OpenAI / other providers.

    raise NotImplementedError(
        "Configure a real LLM provider or use the dummy mode (LLM_PROVIDER=dummy)."
    )
