from flask import Flask, request, render_template, redirect, url_for, session, flash, jsonify
#Importando o regex e o bcrypt para encriptação
import bcrypt
import re

app = Flask(__name__)
users = []  # Lista para armazenar os usuários e suas informações

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

#Uma função que verifica se o username é valido, ou seja, se nao possui espaços ou virgulas
def is_valid_username(username):
    regex = r"^[^ ,]+$"
    return bool(re.match(regex, username))

#Parseando a classe 'user' em json
@app.route('/user') 
def get_users():
    user_data = []
    for user in users:
        user_info = {
            'name': user.username,
            'role': user.role,
        }
        user_data.append(user_info)

    return jsonify({'users': user_data})

#Adicionando usuário ao array
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
    return jsonify ({'message': 'Fail to add user'}), 400
   
@app.route('/admin/login', methods=['POST']) 
def login_user():
    name = request.form.get('name')
    password = request.form.get('password')
    role = request.form.get('role')

    return jsonify({'users': user_data})

# Rota de login - lembrando que é necessário fazer o cadastro antes
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    user = next((user for user in users if user.username == username), None)

    if user and user.check_password(password.encode('utf-8')):
        if user.is_admin():
            return jsonify({'message': 'Admin login successful'}), 200
        else:
            return jsonify({'message': 'Only admin users can log in as an admin'}), 403
    else:
        return jsonify({'message': 'Invalid login credentials'}), 401


#Testado e validado através do POSTMAN ( ferramenta de desenvolvimento de API que permite testar, documentar e colaborar em seus serviços web e APIs. Ele oferece uma interface de usuário fácil de usar para criar, enviar e receber solicitações HTTP, bem como visualizar as respostas das APIs.)

if __name__== '__main__':
    app.run()