# Prompt Injection Gym

A tiny, reproducible playground to **attack** and **defend** a tool-using LLM agent.

Built with:
- Streamlit (UI)
- LangChain + LangGraph (agent + control flow)
- Groq (LLM backend)

## What you get
- Multiple **tasks** with a hidden per-run `SECRET`
- Multiple **defenses** (system hardening, tool allowlist, output redaction)
- Automatic **judge + score** (did the model leak the secret / attempt sensitive tools?)
- Downloadable **trace** (JSON) for replay/debugging

## Setup

Create a virtualenv and install deps:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Set env vars (recommended: copy `env.example` → `.env`):

```bash
copy env.example .env
```

Edit `.env` and set:
- `GROQ_API_KEY`
- `MODEL_NAME`

Run:

```bash
streamlit run app.py
```

## Notes
- `.env` is ignored by git via `.gitignore`. **Do not commit secrets**.
- If you accidentally committed a key, rotate it immediately.

