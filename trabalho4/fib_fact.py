from flask import Flask, request, jsonify

app = Flask(__name__)

def fatorial(n):
    #Verificando se o número é negativo
    if n < 0:
        return 'Número negativo, input inválido'
    #Verificando se o número é inteiro, verifica também se é um caractere 
    elif not isinstance(n, int):
        return 'Número não inteiro, input inválido'
    elif n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n-1)

def fibonacci(n):
    #Verificando se o número é negativo
    if n < 0:
        return 'Número negativo, input inválido'
    elif not isinstance(n, int):
    #Verificando se o número é inteiro, verifica também se é um caractere
        return 'invalid input (non-integer)'
    elif n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequencia_fibonacci = [0, 1]
        while len(sequencia_fibonacci) < n:
            proximo_numero = sequencia_fibonacci[-1] + sequencia_fibonacci[-2]
            sequencia_fibonacci.append(proximo_numero)
        return sequencia_fibonacci

@app.route('/api', methods=['POST'])
def calcular_operacoes():
    data = request.get_json()

    if 'fact' not in data and 'fib' not in data:
        return jsonify({'error': 'unrecognized command'})

    result = {}

    if 'fact' in data:
        try:
            n = int(data['fact'])
            result['fact'] = fatorial(n)
        except ValueError:
            result['fact'] = 'invalid input (non-integer)'

    if 'fib' in data:
        try:
            n = int(data['fib'])
            result['fib'] = fibonacci(n)
        except ValueError:
            result['fib'] = 'invalid input (non-integer)'

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
