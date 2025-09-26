# Criar arquivos, recebendo informação do Usuário

# Solicitação de entrada
nome = input("Digite seu nome completo: ")
email = input("Digite seu email: ")

# Criar arquivo
arquivo = open('pessoa.txt','a',encoding='utf-8')     # estamos criando arquivo
# armazenando na variavel arquivo, o modo 'a' escreve sempre no final, 
# enconding uft- 8 é para ultilizar o conjunto de caracteres que engloba 
# a lingua portuguesa
arquivo.write(nome +'|'+ email + '\n') # .write é para escrever
# \n é para pular linha
arquivo.close() # .close é para fechar o arquivo


