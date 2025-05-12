from unittest.mock import patch

from agents_for_all.llms.openai import OpenAIModel


def test_openai_model_get_response_strips_think_tag():
    class MockMessage:
        content = "Hello <think>internal</think> world"

    class MockChoice:
        message = MockMessage()

    class MockResponse:
        choices = [MockChoice()]

    class MockChatCompletions:
        def create(self, **kwargs):
            return MockResponse()

    class MockClient:
        chat = type("Chat", (), {"completions": MockChatCompletions()})()

    # Patch the OpenAI client constructor to return our fake client
    with patch("openai.OpenAI", return_value=MockClient()):
        model = OpenAIModel(api_key="fake-key", model="gpt-4")
        result = model.get_response("Hello")

    assert result == "Hello  world"
