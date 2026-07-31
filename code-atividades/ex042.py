import math
num = int(input("Digite um número:"))
if num < 0:
    print("Fatorial só é definido para números inteiros não negativos.")
else:
    print(f"O fatorial {num} é", math.factorial(num))
