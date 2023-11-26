import bcrypt

def encrypt_password(password):
    # Função para criptografar a senha através do bcrypt
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def check_password(input_password, stored_password):
    # Função para verificar se a senha fornecida coincide com a senha criptografada
    return bcrypt.checkpw(input_password.encode('utf-8'), stored_password)

def main():

    # Ler a senha armazenada criptografada no arquivo "senha_armazenada.txt"
    with open("senha_armazenada.txt", "rb") as file:
        stored_password = file.read().strip()

    # Ler a senha fornecida pelo usuário do arquivo
    # Neste arquivo "senha_input_incorreta.txt" é armazenado a senha a qual é fornecida pelo o usuário 
    # Após, o script, em python, utiliza-o para inserir na comparação com a senha armazenada
    with open("senha_input_incorreta.txt", "r") as file:
        user_input_password = file.read().strip()

    # Senha que o usuário solicitou armazenada no arquivo txt "senha_input_incorreta.txt"
    password = "senha_input_incorreta.txt"

    # Hash da senha a qual o usuário solicitou armazenada no arquivo txt "senha_input_correta.txt"
    hash_password = encrypt_password(password)

    # Verificando se a senha fornecida coincide com a senha armazenada no "senha_armazenada.txt"
    if check_password(user_input_password, stored_password):
        print(f"Senha fornecida: {user_input_password}")
        # Mostra o hash gerado através da senha fornecida pelo usuário armazenada no arquivo txt "senha_input_correta.txt"
        print("Senha Encryptada:")
        print("Senha correta!")

    else:
        print(f"Senha fornecida: {user_input_password}")
        print("Senha Encryptada:", hash_password.decode('utf-8'))        
        print("Senha incorreta!")

if __name__ == "__main__":
    main()
