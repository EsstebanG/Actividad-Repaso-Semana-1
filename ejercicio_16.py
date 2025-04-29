numeros = [1, 2, 4, 6, 8, 20]

buscador = int(input("Digite un número del 1 al 30 para saber si es uno de los 6 elegidos: "))
poscicion = numeros.index(buscador)


if buscador <= 0 or buscador > 30:
    print("ERROR. Recuerde que el rango es entre 1 y 30.")
else:
    if buscador in numeros:
        poscicion += 1
        print(f"Lista de números elegidos: {numeros}")
        print(f"El número {buscador} está entre los elegidos y está en la poscisión {poscicion}.")
    else:
        print("No lo está.")