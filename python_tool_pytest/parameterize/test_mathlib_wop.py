import mathlib

# Test Case - 1

def test_calc_square_1( ):
    result = mathlib.calc_square(5)
    assert result == 25

# Test Case - 2

def test_calc_square_2( ):
    result = mathlib.calc_square(6)
    assert result == 36

# Test Case - 3

def test_calc_square_3( ):
    result = mathlib.calc_square(7)
    assert result == 49

# Test Case - 4

def test_calc_square_4( ):
    result = mathlib.calc_square(8)
    assert result == 64
