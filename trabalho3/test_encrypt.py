# Este arquivo é somente para fins de análise, ou seja, analise de como 
# o bcrypt faz as encriptações.

import bcrypt

def hash_password(password):
    # Gera um salt aleatório
    # Salt é um valor aleatório único que é gerado para cada senha antes da
    # aplicação do algoritmo de hash. O objetivo principal do salt é 
    # aumentar a segurança do processo de hashing.
    salt = bcrypt.gensalt()

    # Hash da senha com o Salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password

def main():
    # Solicita a senha ao usuário
    password = input("Digite sua senha: ")

    # Hash da senha
    hashed_password = hash_password(password)

    # Mostra o hash gerado
    print("Senha Hash:", hashed_password.decode('utf-8'))

if __name__ == "__main__":
    main()
