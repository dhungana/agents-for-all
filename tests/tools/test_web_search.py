from agents_for_all.tools.web_search import WebSearch
from unittest.mock import patch

def test_google_search_mock():
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = {
            "items": [{"title": "Result", "link": "http://example.com"}]
        }
        tool = WebSearch("google", api_key="dummy", cx="cx")
        result = tool.execute({"query": "test"})
        assert "http://example.com" in result

def test_bing_search_mock():
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = {
            "webPages": {"value": [{"name": "BingResult", "url": "http://bing.com"}]}
        }
        tool = WebSearch("bing", api_key="dummy")
        result = tool.execute({"query": "test"})
        assert "http://bing.com" in result