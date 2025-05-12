from agents_for_all.tools.file import File


def test_file_write_and_read(tmp_path):
    test_file = tmp_path / "sample.txt"
    tool = File()
    write_result = tool.execute(
        {"operation": "write", "path": str(test_file), "content": "Hello File"}
    )
    assert "Wrote" in write_result

    read_result = tool.execute({"operation": "read", "path": str(test_file)})
    assert "Hello File" in read_result
