from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

# operators used on the calculator
OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """
    calcule une expression arithmétique simple entre deux opérateurs binaires.
    utilise un des opérateurs suivants: +, -, * ou /.
    l'opération doit se faire entre deux nombres.
    les espaces sont ignorés.

    Args: 
        expr (str): expression d'entrée comme: "2 + 2" or "3/1.5"

    Returns:
        float: resultat de l'opération et les deux opérandes de l'expression
    
    Raises:
        ValueError: si l'expression n'est pas une chaîne de caractère, si l'expression est vide, 
        si l'expression contient plus qu'un opérateur ou si les opérandes ne sont pas nes nombres valides

    Examples:
        >>> calculate("2 + 2")
            4
        >>> calculate("4/3")
            0.75
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
    """
    Sert une calculatrice web et évalue le résultat d'expressions simples.

    Lors d'une requête GET: fourni le rendu de la calculatrice vide.
    Lors d'une requête POST: récupère l'expression du champ 'display' de la requête, évalue le résultat.
    avec la fonction 'calculate' et fourni le rendu de la page avec le résultat.

    Returns:
        str: retourne le rendu de la page html avec le résultat de l'entrée qui prend la forme d'un
        nombre, d'une champs vide dans si la requête est un GET ou une erreur si l'entrée ne respecte
        pas le format attendu.
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