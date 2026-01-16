# ai365-agentic_tool_calling_dapp
A minimal, educational agentic demo showcasing dynamic tool discovery, LLM‑driven function calling, safe parameter parsing, and Python tool execution.  
Now fully integrated with **Groq** for real LLM-powered tool-calling.

This project is intentionally simple, transparent, and modular — ideal for learning, teaching, and extending into more advanced agentic systems.



## Architecture
```

    subgraph User
        A[ User Query ]
    end

    subgraph Core
        B[ Prompt Builder
            • Builds system prompt
            • Lists tools & signatures ]
        C[ LLM Client
            • Dummy mode (offline)
            • Groq mode (real LLM) ]
        D[ Parser
            • Extracts function name
            • Parses parameters safely ]
        E[ Executor
            • Runs Python function
            • Returns result ]
    end

    subgraph Tools
        F[ Math Tools
            plus/minus/multiply/divide/power/modulo ]
        G[ String Tools
            to_upper/to_lower/concat ]
    end

    A --> B --> C --> D --> E
    E --> A

    D --> F
    D --> G

```



## Runtime Flow
```

sequenceDiagram
    autonumber

    participant U as User
    participant PB as Prompt Builder
    participant LLM as LLM Interface (Groq or Dummy)
    participant P as Tool‑Call Parser
    participant EX as Executor
    participant T as Tools (Python Functions)

    U->>PB: 1. Send natural language query
    PB->>LLM: 2. Build system prompt + tool list<br/>Send to LLM
    LLM-->>P: 3. Return tool‑call text<br/>e.g., "power - {'a':2,'b':8}"
    P->>P: 4. Parse function name + parameters<br/>Safely (literal_eval)
    P->>EX: 5. Pass parsed call to executor
    EX->>T: 6. Execute correct Python function
    T-->>EX: 7. Return computed result
    EX-->>U: 8. Deliver final answer

```



## Folder Structure
```

ai365-agentic_tool_calling_dapp/
│
├── tools/
│   ├── math_tools.py           # arithmetic tools
│   ├── string_tools.py         # text manipulation tools
│   └── __init__.py
│
├── core/
│   ├── tool_registry.py        # auto-detects tools dynamically
│   ├── prompt_builder.py       # builds system prompt
│   ├── llm_client.py           # dummy + Groq integration
│   ├── parser.py               # safe tool-call parsing
│   └── executor.py             # executes selected tool
│
├── examples/
│   ├── simple_math_demo.py
│   ├── power_demo.py
│   └── modulo_demo.py
│
├── app.py                      # CLI entry point
├── README.md
└── requirements.txt

```



## LLM Integration

### **Dummy Mode (default)**  
Offline, deterministic, no API keys needed.

```
export LLM_PROVIDER=dummy
```

### **Groq Mode (real LLM)**  
Uses `llama-3.1-8b-instant` for fast, accurate tool-calling.

```
export LLM_PROVIDER=groq
export GROQ_API_KEY="your_groq_api_key_here"
```



## How It Works

1. User sends a natural language query.  
2. Prompt builder constructs a system prompt listing all tools.  
3. LLM returns a strict tool‑call string:  
   ```
   power - {'a': 2, 'b': 8}
   ```
4. Parser safely extracts the function + parameters.  
5. Executor runs the correct Python function.  
6. Result is returned to the user.  

This mirrors how modern agent frameworks (LangChain, CrewAI, MCP, PydanticAI) implement tool-calling — but in a minimal, transparent way.



## Design Goals

- ✅ Minimal and educational  
- 🔍 Transparent tool-calling flow  
- 🧠 Agentic reasoning foundation  
- 🔧 Easily extensible with new tools  
- 🛡️ Safe parameter parsing (no eval)  
- ⚡ Real LLM integration via Groq  
- 🧩 Clean modular architecture  



## Next Steps (Roadmap)

- Multi-step agentic reasoning  
- RAG tools  
- Web tools  
- File tools  
- Logging & tracing  
- Web UI (FastAPI + HTMX)  
- Unit tests  



