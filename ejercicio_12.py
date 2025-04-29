frutas = ["Mango", "Pera", "Arroz"]

print(f"Lista de frutas: {frutas}")
eliminar = str(input("Digite el nombre de la fruta que desea eliminar de la lista (Tal cual está escrita en la lista): "))

if eliminar in frutas:
    frutas.remove(eliminar)
    print("Fruta eliminada.")
else:
    print("La fruta que escribiste no está en la lista.")

print(f"La lista de frutas actualizadas es: {frutas}")