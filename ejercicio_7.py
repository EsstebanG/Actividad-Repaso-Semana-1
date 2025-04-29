licencia = str(input("Tienes licencia?: "))

casco = str(input("Tienes casco?: "))

if casco != "si" or licencia != "si":
    print("No puedes conducir.")
else:
    print("Puedes conducir.")