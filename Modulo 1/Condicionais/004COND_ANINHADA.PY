#tipo de triângulo
#croe um programa que receba três lados de um triangulo
#verifique se os lados realmente podem formar um triangulo
# e determine os triângulos em:
#equilatero (todos os lados são iguais)
#isósceles (dois lados iguais)
#escaleno(todos os lados diferentes)

a = int(input("Digite o valor do lado a:"))
b = int(input("Digite o valor do lado b:"))
c = int(input("Digite o valor do lado c:"))

#Verificar se os lados formam um triangulo:
if a + b > c and a + c > b and b + c > a: # condicação para formação do triângulo
    if a == b:
      if b == a:
        print (f"Os lados do triângulo são {a}, {b} e {c}: Triângulo Equilátero")
      else:
         print (f"Os lados do triângulo são {a}, {b} e {c}: Triângulo isóceles")
    else:# não é possivel formar um triângulo
        if b == c or a == c :
            print(f"Os Lados do triângulo são {a}, {b} e {c}: Triângulo Isóceles")
        else:
            print(f"Os lados do triângulo são {a}, {b} {c}: Triângulo Escaleno")
else:
   print("Os lados não formam um triângulo válido.")

    
