import pytest

@pytest.mark.parametrize("num, result", [ (1, 11), (2, 22), (3, 33), (4, 44), (5, 55) ])
def test_multiply(num, result):
    assert 11 * num == result
