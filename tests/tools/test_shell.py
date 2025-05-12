from agents_for_all.tools.shell import Shell

def test_shell_executes_ls():
    tool = Shell()
    result = tool.execute({"command": "echo hello"})
    assert "hello" in result