
"""Tests de structure de l'interface HTML de la calculatrice.

Vérifie la présence des boutons, leurs libellés et
les actions JavaScript associées.
"""

import re

import pytest

from app import app


@pytest.fixture
def html():
    """Récupère le HTML de la page principale.

    Args:
        Aucun.

    Returns:
        str: Contenu HTML de la calculatrice.
    """
    app.config["TESTING"] = True

    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200
        return response.get_data(as_text=True)


def get_buttons(html):
    """Extrait les boutons et leurs attributs du HTML.

    Args:
        html (str): Code HTML à analyser.

    Returns:
        list[tuple[str, str]]: Attributs et libellés des boutons.
    """
    return re.findall(
        r"<button\b([^>]*)>(.*?)</button>",
        html,
        flags=re.DOTALL | re.IGNORECASE,
    )


@pytest.mark.parametrize("digit", list("0123456789"))
def test_digit_button_labels(html, digit):
    """Vérifie que chaque chiffre possède son propre libellé.

    Args:
        html (str): Interface HTML.
        digit (str): Chiffre recherché.

    Returns:
        None: Le test réussit si le libellé est correct.
    """
    buttons = get_buttons(html)

    matching = [
        label.strip()
        for attrs, label in buttons
        if f"appendToDisplay('{digit}')" in attrs
    ]

    assert matching == [digit]


@pytest.mark.parametrize("operator", ["+", "-", "*", "/"])
def test_operator_button_labels(html, operator):
    """Vérifie que les opérateurs sont visibles.

    Args:
        html (str): Interface HTML.
        operator (str): Opérateur recherché.

    Returns:
        None: Le test réussit si son libellé est correct.
    """
    buttons = get_buttons(html)

    matching = [
        label.strip()
        for attrs, label in buttons
        if f"appendToDisplay('{operator}')" in attrs
    ]

    assert matching == [operator]


def test_clear_button(html):
    """Vérifie la présence du bouton d'effacement.

    Args:
        html (str): Interface HTML.

    Returns:
        None: Le test réussit si le bouton C est présent.
    """
    buttons = get_buttons(html)

    assert any(
        "clearDisplay()" in attrs and label.strip() == "C"
        for attrs, label in buttons
    )


def test_submit_button(html):
    """Vérifie la présence du bouton de calcul.

    Args:
        html (str): Interface HTML.

    Returns:
        None: Le test réussit si le bouton = soumet le formulaire.
    """
    buttons = get_buttons(html)

    assert any(
        'type="submit"' in attrs and label.strip() == "="
        for attrs, label in buttons
    )


def test_display_field(html):
    """Vérifie le champ d'affichage de la calculatrice.

    Args:
        html (str): Interface HTML.

    Returns:
        None: Le test réussit si le champ attendu existe.
    """
    assert 'id="display"' in html
    assert 'name="display"' in html
    assert "readonly" in html
