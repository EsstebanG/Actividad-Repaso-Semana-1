edad = float(input("Digita su edad actual: "))


if edad <= 8:
    print("Eres un niño.")
elif edad > 8 and edad <= 14:
    print("Eres adolescente.")
elif edad > 14 and edad <= 55:
    print("Eres adulto.")
elif edad >= 55 and edad < 100:
    print("Eres anciano.")
else:
    print("Digite una edad dentro del rango (1 a 100).")