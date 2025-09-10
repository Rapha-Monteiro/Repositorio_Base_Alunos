# 1. Verificação de números diferentes
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
if num1 != num2:
    print("Os números são diferentes")
else:
    print("Os números são iguais")

# 2. Verificação de maioridade
idade = int(input("\nDigite sua idade: "))
if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")

# 3. Autorização de entrada em um evento
convite_valido = input("\nVocê tem um convite válido? (s/n): ").lower()
if convite_valido == "sim":
    print("Entrada permitida")
else:
    print("Entrada negada")

# 4. Verificação de nome em lista
nome = input("\nDigite seu nome: ")
if nome == "Raphael":
    print("Você está na lista")
else:
    print("Nome não encontrado")

# 5. Cálculo de gorjeta
valor_conta = float(input("\nDigite o valor da conta: R$ "))
if valor_conta > 100:
    total = valor_conta * 1.10
else:
    total = valor_conta * 1.05
print(f"Total a pagar com gorjeta: R$ {total:.2f}")

# 6. Acesso ao Wi-Fi
senha = input("\nDigite a senha do Wi-Fi: ")
if senha == "senha123":
    print("Conectado")
else:
    print("Senha incorreta")

# 7. Verificação de turno
turno = input("\nDigite 'M' para manhã ou qualquer outra tecla para tarde: ").upper()
if turno == "M":
    print("Bom dia!")
else:
    print("Boa tarde!")

# 8. Verificação de múltiplo de 5
numero = int(input("\nDigite um número: "))
if numero % 5 == 0:
    print("Múltiplo de 5")
else:
    print("Não é múltiplo de 5")

# 9. Desconto em compras por valor mínimo
valor_compra = float(input("\nDigite o valor da compra: R$ "))
if valor_compra > 150:
    valor_final = valor_compra - 20
    print(f"Desconto aplicado. Total a pagar: R$ {valor_final:.2f}")
else:
    print(f"Sem desconto. Total a pagar: R$ {valor_compra:.2f}")