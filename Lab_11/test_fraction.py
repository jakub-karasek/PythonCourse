import pytest
from unittest.mock import mock_open, patch
from fraction import Fraction

@pytest.fixture
def example_fraction():
    return Fraction(3, 4)

# PARAMETERIZED ARITHMETIC TESTS
@pytest.mark.parametrize("num1, den1, num2, den2, expected_num, expected_den", [
    (1, 2, 1, 3, 5, 6),   # 1/2 + 1/3 = 5/6
    (2, 3, 3, 4, 17, 12), # 2/3 + 3/4 = 17/12
    (1, 2, -1, 2, 0, 1),  # 1/2 + (-1/2) = 0/1
])
def test_fraction_add(num1, den1, num2, den2, expected_num, expected_den):
    f1 = Fraction(num1, den1)
    f2 = Fraction(num2, den2)
    result = f1 + f2
    assert result.numerator == expected_num
    assert result.denominator == expected_den

@pytest.mark.parametrize("num1, den1, num2, den2, expected_num, expected_den", [
    (1, 2, 1, 3, 1, 6),      # 1/2 - 1/3 = 1/6
    (2, 3, 3, 4, -1, 12),    # 2/3 - 3/4 = -1/12
    (1, 2, -1, 2, 1, 1),     # 1/2 - (-1/2) = 1/1
])
def test_fraction_sub(num1, den1, num2, den2, expected_num, expected_den):
    f1 = Fraction(num1, den1)
    f2 = Fraction(num2, den2)
    result = f1 - f2
    assert result.numerator == expected_num
    assert result.denominator == expected_den

@pytest.mark.parametrize("num1, den1, num2, den2, expected_num, expected_den", [
    (1, 2, 1, 3, 1, 6),    # 1/2 * 1/3 = 1/6
    (2, 3, 3, 4, 1, 2),    # 2/3 * 3/4 = 6/12 -> 1/2
    (-1, 2, 1, 2, -1, 4),  # -1/2 * 1/2 = -1/4
])
def test_fraction_mul(num1, den1, num2, den2, expected_num, expected_den):
    f1 = Fraction(num1, den1)
    f2 = Fraction(num2, den2)
    result = f1 * f2
    assert result.numerator == expected_num
    assert result.denominator == expected_den

@pytest.mark.parametrize("num1, den1, num2, den2, expected_num, expected_den", [
    (1, 2, 1, 3, 3, 2),    # (1/2) / (1/3) = (1*3)/(2*1) = 3/2
    (2, 3, 3, 4, 8, 9),    # (2/3) / (3/4) = (2*4)/(3*3) = 8/9
    (-1, 2, 1, 2, -1, 1),  # (-1/2) / (1/2) = (-1*2)/(2*1) = -2/2 -> -1/1
])
def test_fraction_div(num1, den1, num2, den2, expected_num, expected_den):
    f1 = Fraction(num1, den1)
    f2 = Fraction(num2, den2)
    result = f1 / f2
    assert result.numerator == expected_num
    assert result.denominator == expected_den

#   FILE SAVE AND LOAD TESTS (WITH MOCKING) 
def test_save_to_file(example_fraction):
    mocked_open = mock_open()
    with patch("builtins.open", mocked_open):
        example_fraction.save_to_file("tmp.txt")

    mocked_open.assert_called_once_with("tmp.txt", 'w', encoding='utf-8')
    handle = mocked_open()
    expected_write = f"{example_fraction.numerator}/{example_fraction.denominator}"
    handle.write.assert_called_once_with(expected_write)

def test_load_from_file():
    mock_content = "5/7"  # Assume the file content is '5/7'
    mocked_open = mock_open(read_data=mock_content)

    with patch("builtins.open", mocked_open):
        fraction_loaded = Fraction.load_from_file("tmp_load.txt")

    mocked_open.assert_called_once_with("tmp_load.txt", 'r', encoding='utf-8')
    assert fraction_loaded.numerator == 5
    assert fraction_loaded.denominator == 7