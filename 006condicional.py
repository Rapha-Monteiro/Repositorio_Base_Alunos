#Crie um código python que peça o valor da conta. Se for maior que R$100,00
#adiciome uma gorjeta de 10% e exiba o total a pagar.
#Caso contrario, adicione uma gorjeta de 5%

#Etapas para resolução
# 1) solicitar o valor da conta para o usuário
# 2) se a conta for maior que 100 adiciomar 10% de gorjeta e apresentar o total a pagar
# 3)se a conta for menor que 100 adiciomar 5% de gorjeta e apresentar o total a pagar

conta = float(input("Digite o valor da conta R$: "))
if conta >= 100:
    conta_final=conta +(conta *0.1)
    print(f"obrigada por sua visita, sua conta é R$ {conta_final}.")
else:
    conta_final = conta +(conta*0.05)
    print(f"obrigada por sua visita, sua conta é R$ {conta_final}.")