from etl.transform import transform_data

def test_transform_data():
    assert transform_data([1, 2, 3]) == [2, 4, 6]
