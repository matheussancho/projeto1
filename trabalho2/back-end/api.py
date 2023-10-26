from flask import Flask, request, render_template, redirect, url_for, session, flash, jsonify
#Importando o regex e o bcrypt para encriptação
import bcrypt
import re


# podemos instalar o Flask e o Bcrypt através dos comandos:
                # pip install flask
                # pip install bcrypt

app = Flask(__name__)
users = []  # Lista para armazenar os usuários e suas informações

@app.route('/')
def index():
    return render_template('index2.html')

#Criando a classe de usuário com as propriedades username, password e role.
class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password)

    def is_admin(self):
        return self.role == 'Admin'

#Função que verifica se o username é valido, ou seja, se não possui caracteres inválidos
def is_valid_username(username):
    regex = r"^[A-Za-z]+$"
    return bool(re.match(regex, username))

#Parseando a classe 'user' em json, ou seja, quando adicionarmos um usuário, após a adição podemos verificar dentro do array (nosso banco de dados)
@app.route('/user', methods=['GET']) 
def get_users():
    user_data = []
    for user in users:
        user_info = {
            'name': user.username,
            'password': user.password,
            'role': user.role,
        }
        user_data.append(user_info)

    return jsonify({'users': user_data})

#Adicionando usuário ao array (banco de dados)
@app.route('/user', methods=['POST'])
def add_user():
    name = request.form.get('name')
    password = request.form.get('password')
    role = request.form.get('role')

    if any(user.username == name for user in users):
        return jsonify({'message': 'Username already registered'}), 400
    
    if name and is_valid_username(name) and password and role:
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        new_user = User(name, hashed_password, role)
        users.append(new_user)
        return jsonify ({'message': 'User added successfully'}), 200
    return jsonify ({'message': 'Fail to add user, name or something gone wrong'}), 400
   

#@app.route('/admin/login', methods=['POST']) 
#def login_user():
#    name = request.form.get('name')
#    password = request.form.get('password')
#    role = request.form.get('role')

#   return jsonify({'users': user_data})


# Rota de login - lembrando que é necessário fazer o cadastro antes
@app.route('/login', methods=['POST'])
def login():
    name = request.form.get('name')
    password = request.form.get('password')

    user = next((user for user in users if user.username == name), None)

# Comparando se o usuário está apto para fazer o login, ou seja, se este está cadastrado no array (banco de dados)
    if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
        return jsonify({'message': 'User logged in successfully'}), 200
    else:
        return jsonify({'message': 'Invalid login credentials'}), 401

#Rota de deleção de usuário
@app.route('/user/delete', methods=['DELETE'])
def delete_user():
    name = request.form.get('name')
    global users
    user_to_delete = next((user for user in users if user.username == name), None)

    if user_to_delete:
        users.remove(user_to_delete)
        return jsonify({'message': 'User deleted successfully'}), 200
    else:
        return jsonify({'message': 'User not found'}), 404

#Rota para fazer o update de senha ou role, lembrando que o nome cadastrado é inalterável
@app.route('/user/update', methods=['PUT'])
def update_user():
    name = request.form.get('name')  
    new_password = request.form.get('new_password')  
    new_role = request.form.get('new_role')  

    user_to_update = next((user for user in users if user.username == name), None)

    if user_to_update:
        if new_password:
            new_hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            user_to_update.password = new_hashed_password

        if new_role:
            user_to_update.role = new_role

        return jsonify({'message': 'User updated successfully'}), 200

    return jsonify({'message': 'User not found'}), 404

#Lembrando que a solicitação feita no POSTMAN deve ser usada os seguintes parâmetros:
    # name: ''
    # new_password: ''
    #

#Testado e validado através do POSTMAN ( ferramenta de desenvolvimento de API que permite testar, documentar e colaborar em seus serviços web e APIs. Ele oferece uma interface de usuário fácil de usar para criar, enviar e receber solicitações HTTP, bem como visualizar as respostas das APIs.)

if __name__== '__main__':
    app.run()