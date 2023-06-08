agenda={}
while True:
    nombre = input("Ingresa el nombre:\n")
    casa = input("Ingresa el numero de casa:\n")
    celular = input("Ingresa el numero de celular\n")
    telefonos={"celular": celular,"casa":casa}
    agenda[nombre]=telefonos.copy
    seguir = input("¿Quieres seguir agregando nombres? (NO/SI)")
    if seguir.upper()== "NO":
        print("Tu agenda:")
        break
print(agenda)


