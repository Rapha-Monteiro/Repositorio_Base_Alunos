#Crie um código em python que peça um número ao usuario
# e exiba "Número par" se ele for divisivel por 2.

# Etapas de resolução

# 1) solicitar um número ao usúario
# 2) verificar se o número é par ou impar
# 3) informar se o número é par ou impar

numero = float(input("Digite um número"))

if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print("O número {numero} é impar.")
    