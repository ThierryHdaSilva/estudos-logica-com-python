import math

numero = int(input("Digite um número:"))
if numero < 0:
    print("Fatorial só é definido para números inteiros não negativos.")
else:
    print("O fatorial desse número é", math.factorial(numero))
