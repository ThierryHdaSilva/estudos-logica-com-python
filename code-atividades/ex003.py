#Crie um programa que calcule o antecessor e sucessor de um número [ OK ]
#Crie um programa que calcule o dobro, triplo e raiz quadrada de um número [ OK ]
#Crie um programa que calcule a média aritmética entre dois números
import math

num1 = int(input("Digite um número:"))
num2 = int(input("Digite o segundo número número:"))

antecessor = num1 -1
sucessor = num1 +1

dobro = num1 * 2
triplo = num1 * 3
# A raiz real só existe para números não negativos.
if num1 < 0:
    raise ValueError("Não é possível calcular a raiz real de um número negativo.")
raiz_quadrada = math.sqrt(num1)  # Equivalente a num1 ** 0.5.
media = (num1 + num2)/2

print(f'O antecessor do número 1 informado é {antecessor} e sucessor o número é {sucessor}. O dobro é {dobro}, o triplo é {triplo} e a sua raiz quadrada é {raiz_quadrada} :')

print(f'A média dos números, {media}')
