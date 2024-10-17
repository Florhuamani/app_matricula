def guardar_datos_alumnos(id,cui,nombre,apellido,numero_celular,programa_estudio,ciclo_academico,email):
    alumno={
            "id":id,
            "cui":cui,
            "nombre":nombre,
            "apellido":apellido,
            "numero_celular":numero_celular,
            "programa_estudio":programa_estudio,
            "ciclo_academico":ciclo_academico,
            "email":email
            }
    lista_alumnos.append(alumno)