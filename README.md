# ai365-agentic_tool_calling_dapp
A minimal, educational agentic demo showcasing dynamic tool discovery, LLM‑driven function calling, safe parameter parsing, and Python tool execution. Designed as a clean foundation for understanding agentic reasoning and building more advanced AI workflows.

## Architecture
```

    subgraph User
        A[User Query]
    end

    subgraph Core
        B[Prompt Builder<br/>• Builds system prompt<br/>• Lists tools & signatures]
        C[LLM Client<br/>• Sends prompt to LLM<br/>• Receives tool-call text]
        D[Parser<br/>• Extracts function name<br/>• Parses parameters safely]
        E[Executor<br/>• Runs Python function<br/>• Returns result]
    end

    subgraph Tools
        F[Math Tools<br/>plus/minus/multiply/divide/power/modulo]
        G[Future Tools<br/>string_tools, web_tools, rag_tools]
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
    participant LLM as LLM Interface
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
│   ├── math_tools.py
│   ├── string_tools.py        # optional future extension
│   └── __init__.py
│
├── core/
│   ├── tool_registry.py       # auto-detect functions + signatures + docs
│   ├── prompt_builder.py      # builds system prompt dynamically
│   ├── llm_client.py          # Groq/OpenAI client wrapper
│   ├── parser.py              # parses "fn - {params}" safely
│   └── executor.py            # executes the selected tool
│
├── examples/
│   ├── simple_math_demo.py    # equivalent to your gist #2
│   ├── power_demo.py          # equivalent to gist #1
│   └── modulo_demo.py
│
├── app.py                     # main CLI entry point
├── README.md
└── requirements.txt

```

## How It Works
[explanation]

## Design Goals
- ✅ Minimal and educational
- 🔍 Transparent tool-calling flow
- 🧠 Agentic reasoning foundation
- 🔧 Easily extensible with new tools
- 🛡️ Safe parameter parsing (no eval)
