# Prompt Injection Gym    
  
    
<img width="1024" height="559" alt="image" src="https://github.com/user-attachments/assets/00443adc-24a4-469e-a076-f272b547585f" />  
   
  
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


<img width="933" height="406" alt="image" src="https://github.com/user-attachments/assets/a9319fbd-94cd-4c41-a252-601790e16870" />

<img width="950" height="429" alt="image" src="https://github.com/user-attachments/assets/c5eb35dc-3610-4501-8736-f71e8a21d253" />

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
















