"""
- Registrar alumnos.
- Generar fichas de matrículas.
- Mostrar la lista de todos los matriculados.
- Filtrar matriculados por programa de estudio.
"""
Lista_Alumnos=[]

Nombre=input("Ingrese su nombre:")
Apellido=input("Ingrese su apellido:")
Nombre2=input("Ingrese su nombre2:")
Apellido2=input("Ingrese su apellido2:")
Lista_Alumnos.append(Nombre)
Lista_Alumnos.append(Apellido)
Alumno={
    "Nombre":Nombre,
    "Apellido":Apellido
}
Alumno2={
    "Nombre":Nombre2,
    "Apellido":Apellido2
}
Lista_Alumnos.append(Alumno)
Lista_Alumnos.append(Alumno2)
#fin del problema

#deseo mostrar un menú con las opciones de agregar un nuevo alumno y salir del programa.
print(Lista_Alumnos)


# Otra manera de resolver .
Lista_Alumnos=[]
while True:
    print("Menu:")
    print("1. Agregar un nuevo alumno")
    print("2. Mostrar lista de alumnos")
    print("3. Salir del programa")
    opcion = input("Ingrese su opción: ")

    if opcion == "1":
        # ingresar datos del estudiante 
        nombre = input("Ingrese el nombre del nuevo alumno: ")
        apellido = input("Ingrese el apellido del nuevo alumno: ")

        # creun un diccionario para un nuevo estudiante 
        nuevo_alumno = {
            "Nombre": nombre,
            "Apellido": apellido
        }

        # añadir un nuevo estudiante a la lista 
        Lista_Alumnos.append(nuevo_alumno)

        print("Alumno agregado")

    elif opcion == "2":
        # mostrara la lista de estudiantes 
        for alumno in Lista_Alumnos:
            print(f"{alumno['Nombre']} {alumno['Apellido']}")

    elif opcion == "3":
        print("Nos vemos luego")
        break
    else:
        print("Opción incorrecta")