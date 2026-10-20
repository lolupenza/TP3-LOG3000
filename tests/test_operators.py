"""
Tests unitaires des fonctions arithmétiques de operators.py.

Chaque fonction est testée avec des cas simples, des nombres négatifs et,
lorsque c'est pertinent, des cas limites (zéro, ordre des opérations, etc).
Les opérandes sont des entiers, car l'interface n'a pas de bouton « . ».
"""

import pytest

from operators import add, subtract, multiply, divide

# ---------- add ----------

def test_add_positive_integers():
    assert add(2, 3) == 5

def test_add_negative_integers():
    assert add(-4, -6) == -10

def test_add_zero_is_neutral():
    assert add(7, 0) == 7


# ---------- subtract ----------

def test_subtract_positive_integers():
    assert subtract(10, 4) == 6

def test_subtract_order_of_operations():
    # a - b, et non b - a
    assert subtract(3, 8) == -5
    

# ---------- multiply ----------

def test_multiply_positive_integers():
    assert multiply(3, 4) == 12

def test_multiply_by_zero():
    assert multiply(9, 0) == 0

def test_multiply_negative_integers():
    assert multiply(-2, -5) == 10


# ---------- divide ----------

def test_divide_integer_result():
    assert divide(10, 2) == 5

def test_divide_result_with_rest():
    # Division entière
    assert divide(7, 2) == pytest.approx(2)

def test_divide_negative_numbers():
    assert divide(-9, 3) == -3

def test_divide_by_zero_raises_error():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
