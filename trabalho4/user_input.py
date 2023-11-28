import requests

def main():
    #While para executar as requisições até que o usuário queira sair.
    while True:
        commands = input("Digite o comando ('fact' para fatorial, 'fib' para Fibonacci, ou 'exit' para sair, separados por vírgula): ").strip().lower()

        if commands == 'exit':
            print('Saindo do programa.')
            break
    #Comandos que o input permite.
        allowed_commands = ['fact', 'fib']
        user_commands = set(commands.split(','))

        if not user_commands.issubset(allowed_commands):
            print('Comando(s) não reconhecido(s)')
            continue

        values = input("Digite o(s) número(s) para calcular {}: ".format(', '.join(user_commands))).strip()

        try:
            values = [int(value) for value in values.split(',')]
        except ValueError:
            print('Entrada inválida (não é um número inteiro)')
            continue
    #Data que é enviada na request
        data = {command: value for command, value in zip(user_commands, values)}
        response = requests.post("http://localhost:5000/api", json=data)

        if response.status_code == 200:
            results = response.json()
            for command, result in results.items():
                print(f"Resultado para '{command}': {result}")
        else:
            print(f"Erro: {response.json()}")

if __name__ == '__main__':
    main()
