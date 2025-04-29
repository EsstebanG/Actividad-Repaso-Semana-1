pares = []

for i in range(5):
    numero = int(input(f"Digite un número: "))

if numero % 2 == 0:
    pares.append(numero)
    print(f"Los números pares son: {pares}")