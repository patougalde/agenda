agenda={} #se crea el diccionario vacio 
while True:
    nombre = input("Ingresa el nombre:\n")
    casa = input("Ingresa el numero de casa:\n")
    celular = input("Ingresa el numero de celular\n")
    dcasa = input("Ingresala dirreccion de casa\n") 
    doficina = input("Ingresala dirreccion de la oficina\n") 
    datos={"celular": celular,"casa":casa,"dcasa":dcasa,"doficina":doficina} #se crea el segundo diccionario con los datos a agregar
    agenda[nombre]=datos.copy() # telefonos.copy hace referencia a el diccionario pero ya se trae los datos
                                  #sin el .copy traeria el diccionario pero cada vez borraria la informacion ya que las referencias no cambiarian                           
    seguir = input("¿Quieres seguir agregando nombres? (NO/SI)")
    if seguir.upper()== "NO":
        print("Tu agenda:")
        break
print(agenda)
