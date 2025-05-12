from agents_for_all.llms.anthropic import AnthropicModel
from unittest.mock import patch, MagicMock


def test_anthropic_model_get_response_strips_think_tag():
    class MockMessage:
        text = "Claude <think>hidden</think> response"

    class MockResponse:
        content = [MockMessage()]

    with patch("anthropic.Anthropic.messages") as mock_messages:
        mock_messages.create.return_value = MockResponse()

        model = AnthropicModel(
            api_key="fake",
            model="claude-test",
            parameters={"max_tokens": 100}
        )

        result = model.get_response("What's up?")

    assert result == "Claude  response"
