## AI Agent Fundamentals first approach

A minimal blueprint for building type-safe AI agents using **Pydantic AI**.

### Purpose

To demonstrate the three fundamentals of agentic workflows:

1. **Structured Reasoning:** Using system prompts to define behavior.
2. **Tool Use:** Enabling the LLM to execute Python functions.
3. **Observability:** Tracing agent logic and costs via Langfuse.

---

### Quick Setup

1. **Install Dependencies**

```bash
uv sync

```

2. **Configure Environment**

```bash
cp .env.example .env
# Add your OPENROUTER_API_KEY and MODEL to .env

```

3. **Run Agent**

```bash
uv run python agent.py

```

---

### Fundamentals Included

- **Framework:** Pydantic AI for structured validation.
- **Inference:** OpenAI for model.
- **Memory:** Context-aware `conversation history`.
- **Tools:** Example `add_numbers` function for computational accuracy.
- **Tracing:** Langfuse integration for production monitoring.
