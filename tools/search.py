"""Placeholder for a web search tool.
In Lab 2 you'll implement actual search functionality here.
"""
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_exa import ExaSearchResults
import os
from dotenv import load_dotenv

load_dotenv()


def duckduckgo_search(query: str) -> str:
    """Search the web using DuckDuckGo search API"""
    return DuckDuckGoSearchRun(name="search-web")


def exa_search(query: str) -> str:
    """Search the web using Exa search API"""
    api_key = os.getenv("EXA_API_KEY")
    if not api_key:
        return "EXA API key not found. Set EXA_API_KEY environment variable."

    try:
        search_tool = ExaSearchResults(exa_api_key=api_key)
        search_results = search_tool._run(
            query=query,
            num_results=5,
            text_contents_options=True,
            highlights=True,
        )
    except requests.exceptions.RequestException as exc:  # pragma: no cover - network errors
        return f"Exa search failed: {exc}"

    if not search_results:
        return "No search results found."

    if isinstance(search_results, list):
        formatted = []
        for item in search_results:
            url = item.get("url", "")
            snippet = ""
            if item.get("highlights"):
                snippet = " ".join(item["highlights"])
            elif item.get("text"):
                snippet = item["text"]
            formatted.append(f"{url}: {snippet}".strip())
        return "\n".join(formatted)

    return str(search_results)