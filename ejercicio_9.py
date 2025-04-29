nota = float(input("Digita tu nota del examen (0 a 10): "))


if nota < 5 or nota <= 0:
    print("No aprobaste.")
elif nota >= 5 and nota <= 7:
    print("Aprobaste.")
elif nota > 7 and nota <= 10:
    print("Sobresaliente.")
else:
    print("Digite una nota dentro del rango.")