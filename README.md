# projeto 1
Primeiro projeto SEL0456

O trabalho consiste em criar:  

* função **main**, a qual deve chamar 3 funções para processar elementos **double float** em uma **array** que tem tamanho facilmente alterável;  
* As funções devem ser localizadas em um único código fonte em um **branch** inicial denomidado por **main**.  


    Ou seja, criou-se 3 funções em um único arquivo **prog.c**, o qual se encontra em `parte-1`
    O programa pode ser executado através do VSCode, onde precisam ser instaladas as seguintes dependências: 
        
        1. Extension C/C++ Microsoft. [VS Marketplace Link] (https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools-extension-pack) 
        
        2. C/C++ Compile Run. [VS Marketplace Link] (https://marketplace.visualstudio.com/items?itemName=danielpinto8zz6.c-cpp-compile-run)
        
        3. Instalar o software MinGW: `sudo apt install mingw-64`

    O programa pode ser executado através de um compilador online, como o [OnlineGDB] (https://www.onlinegdb.com/online_c_compiler) 

* Seguindo devemos criar um novo **branch** (nesse caso foi parte-2), e modificar o programa para que cada função esteja localizada em um arquivo ".c" diferente, 4 arquivos portanto.  

    Ou seja, podemos encontrar essa divisão dos arquivos na `parte-2`, seguindo as mesmas instruções de execução da `parte-1`.

# Projeto 2

Segundo projeto SEL0456

O trabalho consiste nos seguintes aspectos:

Sistema de cadastro, login e logout de usuários, utilizando o framework **Django** e o banco de dados **MySQL**

- Criar um **Objeto** (ou uma **Classe**) em Python:
    - A Classe em si será para o controle de usuário: 
		- Esta deve conter o *nome* do usuário (login); 
			- *Obs.: Adicionar regras de verificação para a criação do nome corretamente  (ex.: não pode ter caracteres como espaço, vírgula, etc)*;
        - Esta deve conter também a *role* do usuário, ou seja, as atribuição que cada usuários contém; 
            - Serão criados 3 níveis (Ex.: Admin, Manager, User);
	- O login do usuário deve conter um password o qual deve ser armazenado como um *hash*, ou seja, não será armazenado o password diretamente no banco de dados, será necessário fazer a conversão deste password para ser armazenado como um *hash* no banco de dados (security); 
	    - O login deve conter métodos de verificação de senha e verificação das atribuições (Ex.: Admin, Manager, User).
		
Estamos construindo uma API de verificação de usuário. 