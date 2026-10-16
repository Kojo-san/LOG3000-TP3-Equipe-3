"""Module principal de l'application de calculatrice web.

Ce module initialise le serveur Flask, définit les opérations
arithmétiques disponibles, analyse les expressions soumises
et gère les requêtes HTTP vers l'interface utilisateur.
"""

from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """Évalue une expression arithmétique contenant deux opérandes.

    L'expression doit contenir exactement un opérateur parmi
    +, -, * et /. Les espaces sont ignorés.

    Args:
        expr (str): Expression à évaluer, par exemple "12 + 5".

    Returns:
        float: Résultat retourné par l'opération sélectionnée.

    Raises:
        ValueError: Si l'expression est vide, mal formée,
            contient plusieurs opérateurs ou des opérandes invalides.
        ZeroDivisionError: Si une division par zéro est effectuée.
    """
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    if op_pos <= 0 or op_pos >= len(s) - 1:
        # operator at start/end or not found
        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():    
    """Gère l'affichage et le traitement de la calculatrice web.

    Traite les requêtes GET pour afficher la calculatrice et les
    requêtes POST pour évaluer l'expression soumise par l'utilisateur.

    Args:
        Aucun argument explicite. Les données sont récupérées
        à partir de l'objet request de Flask.

    Returns:
        str: Page HTML générée à partir du modèle index.html,
        contenant le résultat du calcul ou un message d'erreur.
    """
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)