# Crie um código que receba 3 notas, calcule a média
#e informe se o aluno está aprovado, em recuperação ou reprovado

#OBS: Aprovado media >=7
# Recuperação média > 4
#Reprovado média > 4

#Etapas 
#1) Solicitar as notas ao usuário
primeira_nota = float(input("Digite a primeira nota"))
segunda_nota = float(input("Digite a segunda nota"))
terceira_nota = float(input("Digite a terceora nota"))

#2) Calcular a média
media = (primeira_nota + segunda_nota + terceira_nota)/3

#3) Checar a condição do aluno
#4) Informar o resultado
if media >=7:
    print(f"O aluno tem média {media} e está aprovado.")
elif media > 4:
    print(f"O aluno teve media {media}e esta em recuperação. ")
else:
    print(f"O aluno teve média {media} e está reprovado.")
     


