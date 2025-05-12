from unittest.mock import patch

from agents_for_all.llms.direct import DirectModel


def test_direct_get_response_strips_think_tag():
    mock_response = {
        "choices": [{"message": {"content": "Hello! <think>invisible</think> World"}}]
    }

    with patch("requests.post") as mock_post:
        mock_post.return_value.json.return_value = mock_response
        direct = DirectModel(api_endpoint="http://fake", model="test-model")
        result = direct.get_response("Hi")

    assert result == "Hello!  World"
