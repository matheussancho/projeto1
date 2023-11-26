import bcrypt

def hash_password(password):
    # Gera um salt aleatório
    salt = bcrypt.gensalt()

    # Hash da senha com o salt
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
