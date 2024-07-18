import mathlib
import pytest

@pytest.mark.parametrize("test_input, expected_output", [ (5, 25), (6, 36), (7, 49), (8, 64) ] )
def test_calc_square(test_input, expected_output):
    result = mathlib.calc_square(test_input)
    assert result == expected_output
