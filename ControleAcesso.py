#GRUPO 93: GABRIELA AYUMI ENDO GONDO

import pyrebase
import os
import stat
import datetime

firebaseConfig = {
    "apiKey": "AIzaSyADNzFkGk5QmzJaEY2v0hW4vqz_qoDXavo",
    "authDomain": "fir-pucpr-49ba4.firebaseapp.com",
    "projectId": "fir-pucpr-49ba4",
    "databaseURL": "https://" + "fir-pucpr-49ba4" + ".firebaseio.com",
    "storageBucket": "fir-pucpr-49ba4.appspot.com",
    "messagingSenderId": "1048578994261",
    "appId": "1:1048578994261:web:e0643da05f853b9e0864dc",
    "measurementId": "G-1Q14BC86V7"
}

user = input("Digite seu e-mail: ")
password = input("Digite sua senha, com pelo menos 6 caracteres: ")

#Inicializando conexão com Firebase usando as credenciais
firebase = pyrebase.initialize_app(firebaseConfig)
#Solicitando autenticação da conexão
auth = firebase.auth()

#Cadastrando o usuário no Firebase
statusCreate = auth.create_user_with_email_and_password(user, password) #Retorna o token do usuário criado com data de validade
idToken = statusCreate["idToken"]
info = auth.get_account_info(idToken) #Armazena a info da conta (usuário, data de criação, email veriificado, etc)


#Enviando email de verificação no Firebase utilizando o token
auth.send_email_verification(idToken)
print("E-mail de verificação enviado: ", user)
confirma = input("Confirma? ")


#Verificando se o email foi verificado
info = auth.get_account_info(idToken)
verifyEmail = info["users"][0]["emailVerified"]
#Realiza-se a autenticação do usuário no Firebase apenas se o email for verificado
if verifyEmail:
    status = auth.sign_in_with_email_and_password(user, password) #Retorna o status do login
    print("Parabéns! Seu usuário foi autenticado.")


    if os.path.isfile("acesso.txt"):
        os.chmod("acesso.txt", stat.S_IRWXU)

    lastLogin = str(datetime.datetime.now())
    dadosAcesso = user + "  " + lastLogin


    arquivo = open("acesso.txt", 'w')
    arquivo.write(dadosAcesso)
    arquivo.close()
    os.chmod("acesso.txt", stat.S_IRUSR)

else:
    print("Verifique seu e-mail.")