nombres = ["Esteban", "Gloria", "Esteban", "Jose", "Esteban", "Gloria"]

print(f"Lista de nombres: {nombres}")
buscador = str(input("Digite el nombre que desea contar en la lista: "))


cantidad = nombres.count(buscador)

if buscador == "Jose":

    print(f"La cantidad de veces que está el nombre Jose en la lista, es: {cantidad} vez.")
else: 
    print(f"La cantidad de veces que está el nombre {buscador} en la lista, son: {cantidad} veces.")