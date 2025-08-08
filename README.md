# AI Agent Workshop Starter

This repository is the hands-on starting point for the **AI Agents for Fun & Profit** workshop.

## Quick start

```bash
# Clone or download the starter kit, then:
make bootstrap        # create virtual-env and install dependencies
cp .env.example .env  # choose provider and add API key
python agent.py       # run the console agent
```

### LLM configuration

Set `LLM_PROVIDER` to `openrouter`, `openai`, or `anthropic` and supply the matching API key:

- `OPENROUTER_API_KEY` for OpenRouter (auto-detected if the key starts with `sk-or-` or `org-`)
- `OPENAI_API_KEY` for OpenAI
- `ANTHROPIC_API_KEY` for Anthropic

If `LLM_PROVIDER` is not set, the application tries to detect OpenRouter keys and otherwise defaults to OpenAI. You can also override the model with `LLM_MODEL`.

## 🎉 New: Streamlit Frontend

Experience your agent through a beautiful web interface:

```bash
# Terminal 1: Start the API
make serve            # FastAPI server at http://localhost:8000

# Terminal 2: Start the Frontend  
make frontend         # Streamlit UI at http://localhost:8501
```

### Features
- 💬 **Interactive Chat Interface** - Chat with your agent in real-time
- 🧠 **Memory Persistence** - Conversations are remembered across messages
- 🔍 **Tool Usage Display** - See when your agent uses search and other tools
- 🔄 **Session Management** - Start new conversations or continue existing ones
- 📊 **Real-time Status** - Monitor API health and agent performance

## Development Commands

```bash
make dev              # Shows how to run both API and frontend
make serve            # Start FastAPI server only
make frontend         # Start Streamlit frontend only
```

## Docker

```bash
make docker-build
make docker-run       # FastAPI server at http://localhost:8000
```

To run both the API and Streamlit frontend, use Docker Compose:

```bash
docker compose up --build  # http://localhost:8000 (API) and http://localhost:8501 (UI)
```

## Workshop Labs

* **Lab 1** ✅ – Basic ReAct agent with LangGraph (no deprecation warnings!)
* **Lab 2** ✅ – Tools implemented: search & math functions
* **Lab 3** – Production-grade deployment with Docker & FastAPI
* **Lab 4** – Add guard-rails (rate-limit & sanitizer)

## Architecture

- **Backend**: FastAPI + LangGraph + pluggable LLM provider
- **Frontend**: Streamlit with real-time chat
- **Agent**: ReAct pattern with tool calling
- **Memory**: Persistent conversation history
- **Tools**: Exa search, math functions (extensible)
