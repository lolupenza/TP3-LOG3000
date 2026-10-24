"""
Tests unitaires des fonctions arithmétiques de operators.py.

Chaque fonction est testée avec des cas simples, des nombres négatifs et,
lorsque c'est pertinent, des cas limites (zéro, ordre des opérations, etc).
La calculatrice doit pouvoir produire des résultats décimaux : on vérifie
donc aussi les opérations sur des opérandes décimaux (app.py les convertit
en float) et les divisions dont le résultat n'est pas entier.
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

def test_add_decimals():
    assert add(1.5, 2.25) == pytest.approx(3.75)

def test_add_decimals_floating_point():
    assert add(0.1, 0.2) == pytest.approx(0.3)


# ---------- subtract ----------

def test_subtract_positive_integers():
    assert subtract(10, 4) == 6

def test_subtract_order_of_operations():
    assert subtract(3, 8) == -5

def test_subtract_decimals():
    assert subtract(5.5, 2.25) == pytest.approx(3.25)

def test_subtract_decimals_negative_result():
    assert subtract(1.2, 3.7) == pytest.approx(-2.5)


# ---------- multiply ----------

def test_multiply_positive_integers():
    assert multiply(3, 4) == 12

def test_multiply_by_zero():
    assert multiply(9, 0) == 0

def test_multiply_negative_integers():
    assert multiply(-2, -5) == 10

def test_multiply_decimals():
    assert multiply(2.5, 4) == pytest.approx(10.0)

def test_multiply_decimals_result():
    assert multiply(1.5, 1.5) == pytest.approx(2.25)


# ---------- divide ----------

def test_divide_integer_result():
    assert divide(10, 2) == 5

def test_divide_result_with_rest():
    assert divide(7, 2) == pytest.approx(3.5)

def test_divide_non_terminating_decimal():
    assert divide(1, 3) == pytest.approx(0.3333333333)

def test_divide_negative_result_with_rest():
    assert divide(-7, 2) == pytest.approx(-3.5)

def test_divide_decimals():
    assert divide(7.5, 2.5) == pytest.approx(3.0)

def test_divide_smaller_by_larger():
    assert divide(2, 8) == pytest.approx(0.25)

def test_divide_negative_numbers():
    assert divide(-9, 3) == -3

def test_divide_by_zero_raises_error():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
