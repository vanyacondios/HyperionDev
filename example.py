import pytest

@pytest.fixture
def dataset():
    """Return some data to test functions"""
    return {'data1': 1, 'data2': 2}

def test_dataset(dataset):
    """test and confirm fixture value"""
    assert dataset == {'data1': 1, 'data2': 2}
    