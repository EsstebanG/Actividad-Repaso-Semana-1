numeros = [1, 2, 3, 4, 5]

agregar = int(input("Digite el número que desea agregar a la lista: "))

poscicion = int(input("¿En que poscición de la lista deseas agregarlo? (0 a 4): "))

numeros.insert(poscicion, agregar)
print(f"La lista con el nuevo dato es: {numeros}")