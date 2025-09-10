# Criar um código python que indique se a temperatura está agradavel ou não
#Condições
#Temperatura >= 30° informar que está muito quente
#Temperatura >= 20° informar que a temperatura está agradável
#temperatura >= 10° informar que está frio

#Etapas para resolução:
# 1) Solicitar a temperatura para o usuário
# 2) verificar a condicional
# 3) imprimir a resposta segundo a temperatura

temperatura =float(input("Digite a temperatura do dia: "))


#if condição
   # bloco de código a ser executado
#elif condição:
   #bloco de código a ser executado
#else:
   # bloco de código a ser executado

if temperatura >= 30:
    print(f"A temperatura do dia é {temperatura}°C e o dia está muito quente")
elif temperatura >= 20:
    print(f"A temperatura do dia é {temperatura}°C e o dia está agradável")
elif temperatura >= 10:
    print(f"A temperatura do dia é {temperatura}°C e o dia está frio")
else:
    print(f"A temperatura do dia é {temperatura}°C e o dia está congelando")