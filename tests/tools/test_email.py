from unittest.mock import patch

from agents_for_all.tools.email import Email


def test_email_mock_smtp():
    with patch("smtplib.SMTP") as mock_smtp:
        instance = mock_smtp.return_value.__enter__.return_value
        tool = Email("smtp.test.com", 587, "user@test.com", "password")
        result = tool.execute(
            {"to": "test@example.com", "subject": "Hello", "body": "This is a test"}
        )
        instance.send_message.assert_called()
        assert "Email sent" in result
