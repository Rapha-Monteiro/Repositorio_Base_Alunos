# Crie um código Python que verifique se a senha digitada
# pelo usuario for "1234", exiba "Acesso permitido"
 
#Etapas para resolução
# criar uma variavel e a atribuir a ela uma senha 
#Através de input solicitar a senha ao usuário
# através da condicional checar se a senha é igual a senha armazenda
# liberar ou não o acesso ao usuário

senha_usuario = "1234"
senha = input("digite sua senha: ")

if senha == senha_usuario: 
    print("Acesso liberado. ")
else:
    print("Acesso negado. Tente novamente")

