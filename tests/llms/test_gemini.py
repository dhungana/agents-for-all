from unittest.mock import patch, MagicMock

from agents_for_all.llms.gemini import GeminiModel

def test_gemini_model_get_response_strips_think_tag():
    mock_response = MagicMock()
    mock_response.text = "Gemini says <think>stuff</think> hello"

    with patch("google.generativeai.GenerativeModel") as mock_model:
        instance = mock_model.return_value
        instance.generate_content.return_value = mock_response

        model = GeminiModel(api_key="key", model="gemini-pro")
        result = model.get_response("say hi")

    assert result == "Gemini says  hello"
