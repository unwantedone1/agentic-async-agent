# agentic-async-agent
# 🧠 Agentic Async Agent with FastAPI + OpenAI

This is a lightweight, async-first agentic AI microservice powered by OpenAI’s SDK and FastAPI. Built for rapid prototyping of API-driven agent workflows.

---

## 🚀 Features

- ⚡️ FastAPI backend with hot reload (via Uvicorn)
- 🔁 AsyncOpenAI client for non-blocking OpenAI calls
- 🧠 Ready for agentic workflows & function calling
- 🌱 Easy to extend and containerize

---

## 🛠️ Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [OpenAI SDK (v1.x)](https://github.com/openai/openai-python)
- [Uvicorn](https://www.uvicorn.org/)

---

## 🧪 Quickstart

1. **Clone the repo**  
   ```bash
   git clone https://github.com/unwantedone1/agentic-async-agent.git
   cd agentic-async-agent

python -m venv .venv
.\.venv\Scripts\activate  # Windows

pip install -r requirements.txt

$env:OPENAI_API_KEY="sk-..."  # PowerShell

uvicorn main:app --reload


---

Let me know if you want badges, Dockerfile notes, or LangChain setup added.
use freely, modify shamelessly.