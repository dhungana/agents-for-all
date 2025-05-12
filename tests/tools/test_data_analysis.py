from agents_for_all.tools.data_analysis import DataAnalysis


def test_data_analysis_sum_column():
    csv = "x,y\n1,2\n3,4"
    tool = DataAnalysis()
    result = tool.execute({"csv": csv, "code": "df['x'].sum()"})
    assert result.strip() == "4"


def test_data_analysis_dataframe_shape():
    csv = "a,b\n1,2\n3,4\n5,6"
    tool = DataAnalysis()
    result = tool.execute({"csv": csv, "code": "df.shape[0]"})
    assert result.strip() == "3"


def test_data_analysis_invalid_code():
    tool = DataAnalysis()
    result = tool.execute({"csv": "a,b\n1,2", "code": "df[nonexistent]"})
    assert "error" in result.lower()
