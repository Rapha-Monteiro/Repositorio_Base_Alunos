#2.Paridade e tamanho do numero

#Crie um código que receba um número inteiro e informe:
#- se é par ou impar
#- e,ao mesmo tempo, se é maior que 10 ou menor ou igual a 10
#Ultilize condicionais aninhadas para organizar as verificações
numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:  
    if numero > 10:
        print("O número é par e maior que 10.")
    else:
        print("O número é par e menor ou igual a 10.")
else:  
    if numero > 10:
        print("O número é ímpar e maior que 10.")
    else:
        print("O número é ímpar e menor ou igual a 10.")


# 3. Classificação por idade
# Faça um progama que leia a idade de uma pessoa e classifique-a em:
# criança : menor que 12 anos
# adolecente: entre 12 e 17 anos
# adulto: maior ou igual a 18 anos
# ultilize a estrutura de condicional aninhada
idade = int(input("Digite a sua idade: "))

if idade < 12:
    print("Criança")
else:
    if idade <= 17:
        print("Adolescente")
    else:
        print("Adulto")
