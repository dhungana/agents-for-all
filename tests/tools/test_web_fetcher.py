from agents_for_all.tools.web_fetcher import WebFetcher
from unittest.mock import patch

def test_web_fetcher_mocks_http():
    with patch("requests.get") as mock_get:
        mock_get.return_value.text = "Mock Page Content"
        tool = WebFetcher()
        result = tool.execute({"url": "http://example.com"})
        assert "Mock Page Content" in result