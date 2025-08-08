import os
from typing import Optional

from langchain_openai import ChatOpenAI

try:
    from langchain_anthropic import ChatAnthropic
except ImportError:  # pragma: no cover - Anthropic optional
    ChatAnthropic = None

OPENROUTER_URL = "https://openrouter.ai/api/v1"


def _detect_openrouter_from_key(key: str) -> bool:
    """Return True if the key appears to be an OpenRouter key."""
    return key.startswith("sk-or-") or key.startswith("org-")


def _select_provider() -> str:
    """Determine the LLM provider based on env vars and key format."""
    provider = os.getenv("LLM_PROVIDER", "").strip().lower()
    openai_key = os.getenv("OPENAI_API_KEY", "")
    openrouter_key = os.getenv("OPENROUTER_API_KEY", "")
    anthropic_key = os.getenv("ANTHROPIC_API_KEY", "")

    if provider:
        return provider

    if openrouter_key or _detect_openrouter_from_key(openai_key):
        return "openrouter"
    if anthropic_key:
        return "anthropic"
    return "openai"


def get_llm():
    """Instantiate an LLM client based on configuration."""
    provider = _select_provider()
    default_models = {
        "openrouter": "qwen/qwen3-coder:free",
        "openai": "gpt-4o-mini",
        "anthropic": "claude-3-haiku-20240307",
    }
    model_name = os.getenv("LLM_MODEL", default_models.get(provider))

    if provider == "openrouter":
        api_key = os.getenv("OPENROUTER_API_KEY") or os.getenv("OPENAI_API_KEY")
        return ChatOpenAI(model_name=model_name, temperature=0, base_url=OPENROUTER_URL, api_key=api_key)
    if provider == "openai":
        api_key = os.getenv("OPENAI_API_KEY")
        return ChatOpenAI(model_name=model_name, temperature=0, api_key=api_key)
    if provider == "anthropic":
        if ChatAnthropic is None:
            raise ImportError("langchain-anthropic is required for Anthropic provider")
        api_key = os.getenv("ANTHROPIC_API_KEY")
        return ChatAnthropic(model_name=model_name, temperature=0, api_key=api_key)
    raise ValueError(f"Unsupported LLM_PROVIDER '{provider}'")
