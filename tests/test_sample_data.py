def test_sample_data_name(sample_data):
    assert sample_data["name"] == "pytest"

def test_sample_data_version(sample_data):
    assert sample_data["version"] == 7.1