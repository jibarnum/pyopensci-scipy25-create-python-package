"""
A test module that tests your example module.

Some people prefer to write tests in a test file for each function or
method/ class. Others prefer to write tests for each module. That decision
is up to you. This test example provides a single test for the example.py
module.
"""

from scipy25_practice_package.example import add_numbers, subtract_numbers, multiply_numbers

def test_add_numbers():
    """
    Test that add_numbers works as expected.

    A single line docstring for tests is generally sufficient.
    """
    out = add_numbers(1, 2)
    expected_out = 3
    assert  out == expected_out, f"Expected {expected_out} but got {out}"

def test_subtract_numbers():
    """
    Test that subtract_numbers works as expeced.
    """
    out = subtract_numbers(1, 3)
    expected_out = -2
    assert out == expected_out, f"Expected {expected_out} but got {out}"

def test_multiply_numbers():
    """
    Test that multiply_numbers works as expeced.
    """
    out = multiply_numbers(1, 3)
    expected_out = -2
    assert out == expected_out, f"Expected {expected_out} but got {out}"