"""Module des opérations arithmétiques de la calculatrice.

Ce module fournit les fonctions permettant d'effectuer les quatre
opérations mathématiques de base : addition, soustraction,
multiplication et division.

Chaque fonction reçoit deux opérandes numériques et retourne
le résultat de l'opération correspondante.
"""

def add(a,b):
    """Calcule la somme de deux nombres.

    Args:
        a (int | float): Premier opérande.
        b (int | float): Deuxième opérande.

    Returns:
        int | float: Somme de a et b.
    """
    return a + b

def subtract(a,b):
    """Calcule la différence entre deux nombres.

    Args:
        a (int | float): Premier opérande.
        b (int | float): Deuxième opérande.

    Returns:
        int | float: Différence attendue entre a et b.
    """
    return a - b

def multiply(a,b):
    """Calcule le produit de deux nombres.

    Args:
        a (int | float): Premier facteur.
        b (int | float): Deuxième facteur.

    Returns:
        int | float: Produit attendu de a et b.
    """    
    return a * b

def divide(a,b):
    """Calcule le quotient de deux nombres.

    Args:
        a (int | float): Dividende.
        b (int | float): Diviseur.

    Returns:
        int | float: Quotient attendu de a par b.

    Raises:
        ZeroDivisionError: Si le diviseur est égal à zéro.
    """
    return a / b
