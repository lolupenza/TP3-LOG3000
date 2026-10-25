import math
import re

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
    Calcule une expression arithmétique composée des opérateurs +, -, * et /.
    La multiplication et la division sont évaluées avant l'addition et la
    soustraction. Les expressions ne peuvent pas contenir d'opérateurs unaires.

    Args: 
        expr (str): expression d'entrée comme "2 + 2", "3/4" ou "2+3*4"

    Returns:
        float: resultat de l'opération et les deux opérandes de l'expression
    
    Raises:
        ValueError: si l'expression est vide, mal formée ou contient des opérandes invalides,
        ou si une division par zéro est demandée

    Examples:
        >>> calculate("2 + 2")
            4
        >>> calculate("3/4")
            0.75
    """
    # soulève une erreur si l'expression n'est pas une chaîne ou est vide
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    # retire les espaces en début et en fin sans fusionner les chiffres
    s = expr.strip()

    operand_pattern = r"\d+(?:[eE]\d+)?"
    token_pattern = re.compile(r"\d+(?:[eE]\d+)?|[+*/-]")
    tokens = []
    position = 0
    for match in token_pattern.finditer(s):
        if s[position:match.start()].strip():
            raise ValueError("operands must be valid numbers")
        tokens.append(match.group())
        position = match.end()
    if s[position:].strip():
        raise ValueError("operands must be valid numbers")

    if len(tokens) < 3 or len(tokens) % 2 == 0:
        raise ValueError("invalid expression format")
    for index, token in enumerate(tokens):
        if index % 2 == 0:
            if not re.fullmatch(operand_pattern, token):
                raise ValueError("operands must be valid numbers")
        elif token not in OPS:
            raise ValueError("invalid expression format")

    try:
        operands = [float(tokens[index]) for index in range(0, len(tokens), 2)]
    except (ValueError, OverflowError) as error:
        raise ValueError("operands must be numbers") from error
    if any(not math.isfinite(operand) for operand in operands):
        raise ValueError("operands must be finite numbers")

    values = [operands[0]]
    operators = []
    for operator, operand in zip(tokens[1::2], operands[1:]):
        if operator == '*':
            values[-1] *= operand
        elif operator == '/':
            try:
                values[-1] = divide(values[-1], operand)
            except ZeroDivisionError as error:
                raise ValueError("division by zero") from error
        else:
            operators.append(operator)
            values.append(operand)

    if not math.isfinite(values[0]) or any(not math.isfinite(value) for value in values):
        raise ValueError("result must be finite")

    result = values[0]
    for operator, value in zip(operators, values[1:]):
        result = OPS[operator](result, value)
    return result

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
    status_code = 200
    # si c'est une requête POST, passe directement à la ligne 101 lors d'une requête GET
    if request.method == 'POST':
        # récupère l'expression dans le champ 'display'
        if 'display' not in request.form:
            return render_template('index.html', result="Error: missing display field"), 400

        expression = request.form['display']
        try:
            # récupère le résultat de 'calculate' avec l'expression d'entrée
            result = calculate(expression)
            if not math.isfinite(result):
                raise ValueError("result must be finite")
        except (ValueError, ZeroDivisionError) as e:
            # enregistre le message d'erreur soulevé par la fonction
            result = f"Error: {e}"
            status_code = 400
    return render_template('index.html', result=result), status_code

if __name__ == '__main__':
    app.run(debug=True)