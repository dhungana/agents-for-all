from agents_for_all.tools.math import Math

def test_math_expression():
    tool = Math()
    result = tool.execute({"expr": "2*x + 1", "x": 3})
    assert "7" in result