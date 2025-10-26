# test_calculator.py

from src.calculator import add

def test_add():
    """
    Tests the add function from the calculator module.
    """
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2
