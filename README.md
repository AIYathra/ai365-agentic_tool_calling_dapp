# 🤖 AI Agentic Tool Calling System

**Note:** "dapp" here means demo app, not decentralized app.

A lightweight, educational framework for building AI agents that can intelligently select and execute tools based on natural language queries. This project demonstrates the fundamentals of agentic reasoning.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

### For Recruiters

This project demonstrates core agentic AI concepts in a minimal, intentionally clean architecture. It highlights dynamic tool discovery, structured function calling, safe execution, and a zero‑friction dual‑mode design (Dummy Mode + Groq Mode). The repo is optimized for readability and educational clarity rather than feature completeness.

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Architecture](#-architecture)
- [Design Decisions](#-design-decisions)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Configuration](#-configuration)
- [Usage Examples](#-usage-examples)
- [Project Structure](#-project-structure)
- [Adding Custom Tools](#-adding-custom-tools)
- [How It Works](#-how-it-works)
- [Available Tools](#-available-tools)
- [Limitations](#-limitations)
- [Possible Extensions (Not Planned)](#-possible-extensions-not-planned)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)
- [Contact](#-contact)
- [Learning Resources](#-learning-resources)
- [Getting Help](#-getting-help)

## 🎯 Overview

This project implements a simple yet powerful agentic AI system that can:
- **Understand** natural language queries
- **Select** appropriate tools from a registry
- **Execute** those tools with extracted parameters
- **Return** results to the user

The system supports two modes:
- **Dummy Mode**: For testing and development (no API key required)
- **Groq Mode**: Production-ready with Llama 3.1 AI models

## ✨ Features

- 🔧 **Automatic Tool Discovery**: Dynamically scans and registers all available tools
- 🧠 **Intelligent Tool Selection**: LLM decides which tool to use based on user query
- 📝 **Type-Safe**: Full type hints for better code quality and IDE support
- 🎨 **Extensible**: Easy to add new tools by creating new functions
- 🔄 **Two Operating Modes**: Dummy (testing) and Groq (production)
- 📚 **Educational**: Well-documented code perfect for learning agentic AI concepts
- ⚡ **Fast**: Uses Groq's optimized inference for quick responses

## 🏗️ Architecture

```
┌─────────────────┐
│   User Query    │
└────────┬────────┘
         │
         ▼
┌─────────────────────────────────────┐
│  1. Build System Prompt             │
│     (List available tools)          │
└────────┬────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────┐
│  2. Call LLM                        │
│     (AI selects tool + params)      │
└────────┬────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────┐
│  3. Parse Response                  │
│     ("power - {'a': 2, 'b': 8}")    │
└────────┬────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────┐
│  4. Execute Tool                    │
│     (Run the actual function)       │
└────────┬────────────────────────────┘
         │
         ▼
┌─────────────────┐
│     Result      │
└─────────────────┘
```

## 🎨 Design Decisions

This project prioritizes **clarity and educational value** through several deliberate architectural choices:

- **Dual‑mode design** (Dummy Mode + Groq Mode) reduces friction for recruiters and enables instant execution without API keys.
- **Dynamic tool discovery** using Python introspection instead of manual tool registration keeps the codebase DRY and scalable.
- **Minimal, intentionally educational architecture** designed to teach agentic tool-calling fundamentals without overwhelming complexity.
- **Clear separation** between LLM reasoning, tool registry, and execution pipeline for maintainability and testability.

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- (Optional) Groq API key for production mode

### Step 1: Clone the Repository

```bash
git clone https://github.com/AIYathra/ai365-agentic_tool_calling_dapp.git
cd ai365-agentic_tool_calling_dapp
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` doesn't exist, install manually:

```bash
pip install groq
```

## ⚡ Quick Start

### Option 1: Dummy Mode (No API Key Required)

Perfect for testing and learning!

```bash
# Set to dummy mode (or don't set LLM_PROVIDER at all)
export LLM_PROVIDER=dummy

# Run a demo
python examples/power_demo.py
```

**Expected Output:**
```
[User query]
Calculate 2 to the power of 8.

[System prompt]
You are a tool-calling assistant...

[LLM raw response]
power - {'a': 2, 'b': 8}

[Parsed tool call] function=power, params={'a': 2, 'b': 8}

[Result]
256
```

### Option 2: Production Mode with Groq AI

```bash
# Step 1: Get your free API key from https://console.groq.com

# Step 2: Set environment variables
export GROQ_API_KEY="gsk_your_actual_api_key_here"
export LLM_PROVIDER=groq

# Step 3: Run the main application
python app.py "What is 15 divided by 3?"
```

### Interactive Mode

```bash
# Run without arguments for interactive mode
python app.py

# You'll be prompted:
# Enter your query: What is the remainder when 100 is divided by 7?
```

## 🔧 Configuration

### Environment Variables

| Variable | Values | Default | Description |
|----------|--------|---------|-------------|
| `LLM_PROVIDER` | `dummy` or `groq` | `dummy` | Selects which AI backend to use |
| `GROQ_API_KEY` | Your API key | None | Required for Groq mode |

### Setting Environment Variables

**macOS/Linux:**
```bash
export GROQ_API_KEY="your_key_here"
export LLM_PROVIDER=groq
```

**Windows (Command Prompt):**
```cmd
set GROQ_API_KEY=your_key_here
set LLM_PROVIDER=groq
```

**Windows (PowerShell):**
```powershell
$env:GROQ_API_KEY="your_key_here"
$env:LLM_PROVIDER="groq"
```

**Using .env file (recommended):**

1. Create a `.env` file in the project root:
```bash
GROQ_API_KEY=gsk_your_actual_key_here
LLM_PROVIDER=groq
```

2. Install python-dotenv:
```bash
pip install python-dotenv
```

3. Load in your code:
```python
from dotenv import load_dotenv
load_dotenv()
```

## 📖 Usage Examples

### Running Individual Demos

```bash
# Test power calculations
python examples/power_demo.py

# Test modulo operations
python examples/modulo_demo.py

# Test multi-step math (shows limitations)
python examples/simple_math_demo.py
```

### Using Command-Line Arguments

```bash
# Single query
python app.py "Calculate 5 to the power of 3"

# Math operations
python app.py "What is 1000 modulo 7?"

# String operations
python app.py "Convert 'hello world' to uppercase"

# Division
python app.py "Divide 100 by 4"
```

### Example Queries That Work

**Math Operations:**
```bash
python app.py "What is 2 to the power of 10?"
python app.py "Find the remainder when 50 is divided by 7"
python app.py "Add 25 and 17"
python app.py "Multiply 6 by 9"
```

**String Operations:**
```bash
python app.py "Convert 'python' to uppercase"
python app.py "Make 'HELLO' lowercase"
python app.py "Combine 'Hello' and 'World'"
python app.py "How long is 'artificial intelligence'?"
```

## 📂 Project Structure

```
ai365-agentic_tool_calling_dapp/
│
├── app.py                      # Main entry point
├── requirements.txt             # Python dependencies
├── README.md                    # This file
│
├── core/                        # Core system modules
│   ├── __init__.py
│   ├── llm_client.py           # LLM API integration
│   ├── parser.py               # Tool call parser
│   ├── executor.py             # Tool execution engine
│   ├── tool_registry.py        # Automatic tool discovery
│   └── prompt_builder.py       # System prompt generation
│
├── tools/                       # Tool implementations
│   ├── __init__.py
│   ├── math_tools.py           # Math operations (6 functions)
│   └── string_tools.py         # String operations (4 functions)
│
└── examples/                    # Demo scripts
    ├── power_demo.py           # Test power calculations
    ├── modulo_demo.py          # Test modulo operations
    └── simple_math_demo.py     # Test multi-step queries
```

### Core Modules Explained

| Module | Purpose | Key Function |
|--------|---------|--------------|
| `llm_client.py` | Communicates with AI | `call_llm_for_tool_call()` |
| `parser.py` | Parses AI responses | `parse_tool_call()` |
| `executor.py` | Executes tools | `execute_tool_call()` |
| `tool_registry.py` | Discovers tools | `get_tool_registry()` |
| `prompt_builder.py` | Builds AI instructions | `build_system_prompt()` |

## 🛠️ Adding Custom Tools

### Step 1: Create a Tool Function

Add to `tools/math_tools.py` or `tools/string_tools.py`:

```python
def factorial(n: int) -> int:
    """Calculate the factorial of n (n!)."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
```

### Step 2: Test It

```python
# Test in Python REPL
from tools.math_tools import factorial

print(factorial(5))  # Output: 120
```

### Step 3: Use It

That's it! The tool is **automatically discovered** and available to the AI.

```bash
python app.py "What is the factorial of 5?"
# AI will respond: factorial - {'n': 5}
# Result: 120
```

### Creating a New Tool Category

**Create `tools/web_tools.py`:**

```python
def search(query: str) -> str:
    """Search the web for information."""
    # Implementation here
    return f"Search results for: {query}"
```

**Update `core/tool_registry.py`:**

```python
from tools import math_tools, string_tools, web_tools  # Add web_tools

def get_tool_registry() -> Dict[str, Callable]:
    registry: Dict[str, Callable] = {}
    registry.update(_collect_functions(math_tools))
    registry.update(_collect_functions(string_tools))
    registry.update(_collect_functions(web_tools))  # Add this line
    return registry
```

## 🧠 How It Works

### The Tool Calling Pipeline

1. **User Query**: "What is 2 to the power of 8?"

2. **System Prompt Generation**:
   ```
   You are a tool-calling assistant.
   Available tools:
   - power: Return a raised to the power of b
   - modulo: Return the remainder when a is divided by b
   ...
   ```

3. **LLM Processing**:
   - AI reads available tools
   - AI understands the query
   - AI selects `power` tool
   - AI extracts parameters: a=2, b=8

4. **LLM Response**:
   ```
   power - {'a': 2, 'b': 8}
   ```

5. **Parsing**:
   ```python
   function_name = "power"
   parameters = {'a': 2, 'b': 8}
   ```

6. **Execution**:
   ```python
   result = power(a=2, b=8)  # Returns 256
   ```

7. **Result**: `256`

## 🔧 Available Tools

### Math Tools (`tools/math_tools.py`)

| Function | Parameters | Description | Example |
|----------|-----------|-------------|---------|
| `plus` | `a: float, b: float` | Addition | `plus(5, 3)` → `8.0` |
| `minus` | `a: float, b: float` | Subtraction | `minus(10, 3)` → `7.0` |
| `multiply` | `a: float, b: float` | Multiplication | `multiply(4, 5)` → `20.0` |
| `divide` | `a: float, b: float` | Division | `divide(20, 4)` → `5.0` |
| `power` | `a: float, b: float` | Exponentiation | `power(2, 8)` → `256.0` |
| `modulo` | `a: int, b: int` | Remainder | `modulo(17, 5)` → `2` |

### String Tools (`tools/string_tools.py`)

| Function | Parameters | Description | Example |
|----------|-----------|-------------|---------|
| `to_upper` | `text: str` | Convert to uppercase | `to_upper("hello")` → `"HELLO"` |
| `to_lower` | `text: str` | Convert to lowercase | `to_lower("WORLD")` → `"world"` |
| `concat` | `a: str, b: str, separator: str = " "` | Join strings | `concat("Hello", "World")` → `"Hello World"` |
| `length` | `text: str` | Get string length | `length("Python")` → `6` |

## ⚠️ Limitations

### Current Limitations

1. **Single Tool Call Only**:
   - Can only execute ONE tool per query
   - Multi-step operations like "Add 10 and 25, then subtract 3" won't work correctly
   - See `simple_math_demo.py` for an example of this limitation

2. **No Conversation Memory**:
   - Each query is independent
   - Can't reference previous results
   - Example: Can't say "Now multiply that by 2"

3. **No Error Recovery**:
   - If AI formats response incorrectly, it fails
   - No retry mechanism

4. **Basic Tool Set**:
   - Limited to math and string operations
   - No file I/O, web access, or database operations

### Future Improvements

See [Roadmap](#roadmap) for planned enhancements.

## 🚀 Possible Extensions (Not Planned)

These are conceptual directions showing how the architecture could evolve. I do not plan to implement them due to time constraints.

- Multi-step tool calling (agent loops with intermediate results)
- Conversation memory and context management
- Retry logic and error recovery mechanisms
- Tool chaining (composing multiple tools in sequence)
- Observability/logging for debugging and monitoring
- Optional UI layer (Streamlit, Gradio, or web interface)

## 🗺️ Roadmap

### Phase 1: Core Improvements
- [ ] Add conversation history/memory
- [ ] Implement multi-turn tool calling (agent loop)
- [ ] Add retry logic for failed API calls
- [ ] Better error handling and user feedback

### Phase 2: Advanced Features
- [ ] Support for OpenAI and Anthropic APIs
- [ ] Add more tool categories (file, web, database)
- [ ] Implement tool chaining (use output of one tool as input to another)
- [ ] Add streaming responses

### Phase 3: Production Ready
- [ ] Add logging and observability
- [ ] Create web UI with Streamlit/Gradio
- [ ] Docker containerization
- [ ] Rate limiting and cost tracking
- [ ] Tool usage analytics

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Adding New Tools

1. Fork the repository
2. Create a new branch: `git checkout -b feature/new-tool`
3. Add your tool to appropriate file in `tools/`
4. Add tests/demos in `examples/`
5. Update this README if needed
6. Submit a pull request

### Reporting Issues

Found a bug? Have a suggestion? Please [open an issue](https://github.com/AIYathra/ai365-agentic_tool_calling_dapp/issues)!

### Code Style

- Follow PEP 8 guidelines
- Add type hints to all functions
- Include docstrings for all public functions
- Keep functions focused and simple

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **Groq** for providing fast, free AI inference
- **Meta** for the Llama 3.1 model
- The open-source AI community for inspiration

## 📞 Contact

- **GitHub**: [@AIYathra](https://github.com/AIYathra)
- **Project Link**: [ai365-agentic_tool_calling_dapp](https://github.com/AIYathra/ai365-agentic_tool_calling_dapp)

---

**⭐ If you found this project helpful, please star it on GitHub!**

## 🎓 Learning Resources

Want to learn more about agentic AI systems?

- [LangChain Documentation](https://python.langchain.com/)
- [OpenAI Function Calling Guide](https://platform.openai.com/docs/guides/function-calling)
- [Anthropic Tool Use Guide](https://docs.anthropic.com/claude/docs/tool-use)
- [Groq Documentation](https://console.groq.com/docs)

## 🚀 Getting Help

### Common Issues

**Issue: `ModuleNotFoundError: No module named 'groq'`**
```bash
# Solution:
pip install groq
```

**Issue: `RuntimeError: GROQ_API_KEY environment variable is not set`**
```bash
# Solution:
export GROQ_API_KEY="your_api_key_here"
```

**Issue: `NotImplementedError: Unknown LLM_PROVIDER`**
```bash
# Solution: Use either 'dummy' or 'groq'
export LLM_PROVIDER=groq
```

### FAQ

**Q: Do I need an API key to test the system?**
A: No! Use dummy mode for testing: `export LLM_PROVIDER=dummy`

**Q: How much does Groq API cost?**
A: Groq offers a generous free tier. Check [console.groq.com](https://console.groq.com) for current limits.

**Q: Can I use OpenAI instead of Groq?**
A: Not yet, but it's on the roadmap! The system is designed to be extensible.

**Q: How do I add my own tools?**
A: Just add a function to `tools/math_tools.py` or `tools/string_tools.py` with a docstring. It's automatically discovered!

---

Made with ❤️ by AIYathra | #AI365 Challenge
