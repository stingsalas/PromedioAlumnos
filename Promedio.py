estudiantes = {"codigo": ["001", "002", "003", "004", "005"],
               "cursos": ["Matematica", "Lenguaje", "Ingles", "Quimica", "Fisica"],
               "nombres": ["Diego", "Daniel", "Maria", "Alejandra"]}
nota_ = []
respuesta = "s"
while respuesta == "s":
    codigoIn = input("Ingresar el codigo del curso: ")
    print("ingresar notas")
    Nota1 = int(input("Nota 1: "))
    Nota2 = int(input("Nota 2: "))
    Nota3 = int(input("Nota 3: "))
    x = 0
    for i in estudiantes["codigo"]:
        if i == codigoIn:
            codigoTemp = i
            cursosTemp = estudiantes["cursos"][x]
            nombresTemp = estudiantes["nombres"][x]
            promedio = (Nota1 + Nota2 + Nota3) / 3
            registro = ["Codigo: " + str(codigoTemp) + " | " + "Nombre: " + str(nombresTemp) + " | " + "Curso: " + str(cursosTemp) + " | " + "Nota 1: " + str(Nota1) + "| " + "Nota 2: " + str(Nota2) + " | " + "Nota 3: " + str(Nota3) + " | "  + "Promedio: " + str(promedio) + " | "]
            f = open("notas.txt", "a")
            cadena = "".join(registro)
            f.write("\n" + cadena)
            f.close()
    x += 1
    respuesta = input("¿Desea seguir ingresando datos? : s/n ")
    f = open("notas.txt")
    print(f.read())
    f.close()

