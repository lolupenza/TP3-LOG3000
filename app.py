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
        expr (str): expression d'entrée comme: "2 + 2" or "3/4"

    Returns:
        float: resultat de l'opération et les deux opérandes de l'expression
    
    Raises:
        ValueError: si l'expression n'est pas une chaîne de caractère, si l'expression est vide, 
        si l'expression contient plus qu'un opérateur ou si les opérandes ne sont pas nes nombres valides

    Examples:
        >>> calculate("2 + 2")
            4
        >>> calculate("3/4")
            0.75
    """
    # soulève une erreur si l'expression n'est pas une chaîne ou est vide
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    # retire les espaces de l'expression
    s = expr.replace(" ", "")

    # mise en place de la lecture de l'expression
    op_pos = -1
    op_char = None

    # passe sur chaque caractère et vérifie si le caractère est l'opérateur et on enregistre la position 
    # de cet opérateur. Si on en trouve un autre, on soulève une erreur.
    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    # si l'opétateur n'est pas trouvé, s'il n'y a pas d'opérande avant ou après l'opérateur, on soulève
    # une exception
    if op_pos <= 0 or op_pos >= len(s) - 1:
        # operator at start/end or not found
        raise ValueError("invalid expression format")

    #opérande de gauche
    left = s[:op_pos]
    #opérande de droite
    right = s[op_pos+1:]

    # on essaie de caster les opérandes en float pour s'assurer que ce sont des nombres
    try:
        a = float(left)
        b = float(right)
    except ValueError:
        # soulève une erreur si au moins une opérande n'est pas un nombre
        raise ValueError("operands must be numbers")

    # appelle l'opérateur avec les deux opérandes et traduit la division par zéro
    try:
        return OPS[op_char](a, b)
    except ZeroDivisionError as error:
        raise ValueError("division by zero") from error

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
    # si c'est une requête POST, passe directement à la ligne 101 lors d'une requête GET
    if request.method == 'POST':
        # récupère l'expression dans le champ 'display'
        expression = request.form.get('display', '')
        try:
            # récupère le résultat de 'calculate' avec l'expression d'entrée
            result = calculate(expression)
        except Exception as e:
            # enregistre le message d'erreur soulevé par la fonction
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)