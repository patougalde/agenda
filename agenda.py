agenda={}
while True:
    nombre = input("Ingresa el nombre:\n")
    telefono = input("Ingresa el numero de telefono:\n")
    agenda[nombre]=telefono
    seguir = input("¿Quieres seguir agregando nombres? (NO/SI)")
    if seguir.upper()== "NO":
        print("Tu agenda\n")
        break
print(agenda)


