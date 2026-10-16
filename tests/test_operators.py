"""Tests unitaires des opérations arithmétiques.

Ce module vérifie que les fonctions de operators.py
respectent le comportement mathématique attendu.
"""

import pytest

from operators import add, subtract, multiply, divide


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 8),
        (0, 0, 0),
        (-4, 6, 2),
        (2.5, 1.5, 4.0),
    ],
)
def test_add(a, b, expected):
    """Vérifie l'addition pour des entiers et des décimaux.

    Args:
        a: Premier opérande.
        b: Deuxième opérande.
        expected: Somme attendue.

    Returns:
        None: Le test réussit si le résultat est correct.
    """
    assert add(a, b) == pytest.approx(expected)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 3, 7),
        (3, 10, -7),
        (5, 0, 5),
        (-4, -2, -2),
    ],
)
def test_subtract(a, b, expected):
    """Vérifie que la soustraction respecte l'ordre des opérandes.

    Args:
        a: Nombre dont on soustrait.
        b: Nombre à soustraire.
        expected: Différence attendue.

    Returns:
        None: Le test réussit si la différence est correcte.
    """
    assert subtract(a, b) == pytest.approx(expected)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (4, 3, 12),
        (5, 0, 0),
        (-2, 3, -6),
        (2.5, 2, 5.0),
    ],
)
def test_multiply(a, b, expected):
    """Vérifie le calcul du produit de deux nombres.

    Args:
        a: Premier facteur.
        b: Deuxième facteur.
        expected: Produit attendu.

    Returns:
        None: Le test réussit si le produit est correct.
    """
    assert multiply(a, b) == pytest.approx(expected)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 2, 5),
        (7, 2, 3.5),
        (-9, 2, -4.5),
        (1, 4, 0.25),
    ],
)
def test_divide(a, b, expected):
    """Vérifie que la division conserve les résultats décimaux.

    Args:
        a: Dividende.
        b: Diviseur non nul.
        expected: Quotient attendu.

    Returns:
        None: Le test réussit si le quotient est correct.
    """
    assert divide(a, b) == pytest.approx(expected)


def test_divide_by_zero():
    """Vérifie que la division par zéro lève une exception.

    Args:
        Aucun.

    Returns:
        None: Le test réussit si ZeroDivisionError est levée.
    """
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
