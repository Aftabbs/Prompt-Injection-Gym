from __future__ import annotations

import os

from dotenv import load_dotenv


def load_env() -> None:
    """Load local .env (if present) into process env."""
    load_dotenv(override=False)


def require_env(name: str) -> str:
    val = os.getenv(name)
    if not val:
        raise RuntimeError(
            f"Missing required environment variable {name!r}. "
            f"Set it in your shell or in a local .env file."
        )
    return val


def get_model_name() -> str:
    # Groq model name is provider-specific; user controls via env.
    return os.getenv("MODEL_NAME", "llama-3.1-70b-versatile")

