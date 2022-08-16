estudiantes = {"codigo": ["001", "002", "003", "004", "005", "006"],
             "cursos": ["matematica", "lenguaje", "quimica", "historia", "ingles", "fisica"],
               "nombre": ["Carlos", "Diego", "Maria", "Rosario", "Angel", "Isabel"]}

listaestudiantes = []
resp = "s"
while resp == "s":
    codigoIn = input("Ingresar el codigo del curso: ")
    x = 0
    for i in estudiantes["codigo"]:
        if i == codigoIn:
            codigoTemp = i
            nombreTemp = estudiantes["nombre"][x]
            cursosTemp = estudiantes["cursos"][x]

    print("ingresar notas")
    Nota1 = int(input("Nota 1: "))
    Nota2 = int(input("Nota 2: "))
    Nota3 = int(input("Nota 3: "))
    promedio = (Nota1 + Nota2 + Nota3)/3

    registro = codigoTemp, nombreTemp, cursosTemp, Nota1, Nota2 , Nota3, promedio
    listaestudiantes.append(registro)
    x += 1
    resp = input("¿Desea seguir ingresando datos? : s/n ")

print("Cod Nombre Curso N.1 / N.2 / N.3 / Promedio")
for x in listaestudiantes:
    print(*x, end="\n")

