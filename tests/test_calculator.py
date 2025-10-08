import pytest
from calculator import (
    addition,
    subtraction,
    multiplication,
    division,
    exponentiation,
    square_root,
)

def test_addition():
    assert addition(2, 3) == 5
    assert addition(-1, 1) == 0
    assert addition(0, 0) == 0
    assert addition(2.5, 3.1) == 5.6

def test_subtraction():
    assert subtraction(5, 3) == 2
    assert subtraction(0, 5) == -5
    assert subtraction(-2, -3) == 1

def test_multiplication():
    assert multiplication(4, 5) == 20
    assert multiplication(-2, 3) == -6
    assert multiplication(0, 100) == 0

def test_division():
    assert division(10, 2) == 5
    assert division(-9, 3) == -3
    assert division(7, 2) == 3.5

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError, match = "Деление на ноль невозможно."):
        division(5, 0)

def test_exponentiation():
    assert exponentiation(2, 3) == 8
    assert exponentiation(5, 0) == 1
    assert exponentiation(4, 0.5) == 2
    assert exponentiation(-2, 3) == -8

def test_square_root():
    assert square_root(4) == 2
    assert square_root(0) == 0
    assert square_root(2.25) == 1.5

def test_square_root_negative():
    with pytest.raises(ValueError, match = "Квадратный корень из отрицательного числа не определён."):
        square_root(-1)