
"""Tests d'intégration de l'application Flask.

Ce module vérifie les routes HTTP, le traitement des expressions
arithmétiques et la gestion des erreurs de la calculatrice.
"""

import pytest

from app import app, calculate


@pytest.fixture
def client():
    """Crée un client Flask pour simuler des requêtes HTTP.

    Args:
        Aucun.

    Yields:
        FlaskClient: Client de test configuré pour l'application.
    """
    app.config["TESTING"] = True

    with app.test_client() as test_client:
        yield test_client


def test_get_index(client):
    """Vérifie que la page principale est accessible.

    Args:
        client: Client de test Flask.

    Returns:
        None: Le test réussit si la réponse HTTP est 200
        et contient le formulaire de la calculatrice.
    """
    response = client.get("/")

    assert response.status_code == 200
    assert b"<form" in response.data


@pytest.mark.parametrize(
    "expression, expected",
    [
        ("5+3", "8.0"),
        ("10-3", "7.0"),
        ("4*3", "12.0"),
        ("7/2", "3.5"),
    ],
)
def test_post_operations(client, expression, expected):
    """Vérifie le traitement des opérations par la route POST.

    Args:
        client: Client de test Flask.
        expression: Expression arithmétique à soumettre.
        expected: Résultat attendu dans la réponse HTML.

    Returns:
        None: Le test réussit si le résultat est affiché.
    """
    response = client.post("/", data={"display": expression})

    assert response.status_code == 200
    assert f'value="{expected}"'.encode() in response.data


@pytest.mark.parametrize(
    "expression, expected",
    [
        ("", "empty expression"),
        ("5+", "invalid expression format"),
        ("+5", "invalid expression format"),
        ("5++3", "only one operator is allowed"),
        ("abc+3", "operands must be numbers"),
    ],
)
def test_post_invalid_expressions(client, expression, expected):
    """Vérifie la gestion des expressions invalides.

    Args:
        client: Client de test Flask.
        expression: Expression invalide soumise.
        expected: Message d'erreur attendu.

    Returns:
        None: Le test réussit si le message d'erreur est affiché.
    """
    response = client.post("/", data={"display": expression})

    assert response.status_code == 200
    assert f'value="Error: {expected}"'.encode() in response.data


def test_post_division_by_zero(client):
    """Vérifie la gestion d'une division par zéro via Flask.

    Args:
        client: Client de test Flask.

    Returns:
        None: Le test réussit si une erreur est affichée.
    """
    response = client.post("/", data={"display": "10/0"})

    assert response.status_code == 200
    assert b"Error:" in response.data
    assert b"division by zero" in response.data


@pytest.mark.parametrize(
    "expression, expected",
    [
        ("5 + 3", 8.0),
        ("10 - 3", 7.0),
        ("4 * 3", 12.0),
        ("7 / 2", 3.5),
    ],
)
def test_calculate_valid_expressions(expression, expected):
    """Vérifie l'analyse et le calcul des expressions valides.

    Args:
        expression: Expression à analyser.
        expected: Résultat mathématique attendu.

    Returns:
        None: Le test réussit si le calcul est correct.
    """
    assert calculate(expression) == pytest.approx(expected)


@pytest.mark.parametrize(
    "expression, error_message",
    [
        ("", "empty expression"),
        ("5+", "invalid expression format"),
        ("5++3", "only one operator is allowed"),
        ("abc+3", "operands must be numbers"),
    ],
)
def test_calculate_invalid_expressions(expression, error_message):
    """Vérifie que calculate rejette les expressions invalides.

    Args:
        expression: Expression invalide.
        error_message: Message d'erreur attendu.

    Returns:
        None: Le test réussit si ValueError est levée.
    """
    with pytest.raises(ValueError, match=error_message):
        calculate(expression)
