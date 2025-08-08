import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from tools import search


def test_duckduckgo_search_executes_tool(monkeypatch):
    calls = {}

    class DummySearch:
        def __init__(self, name=None):
            pass

        def run(self, query):
            calls['query'] = query
            return f"result for {query}"

    monkeypatch.setattr(search, 'DuckDuckGoSearchRun', lambda name="search-web": DummySearch(name))

    result = search.duckduckgo_search("python")
    assert result == "result for python"
    assert calls['query'] == "python"


