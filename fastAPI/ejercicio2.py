notas_alumnos: dict[str, int] = {
    "Ana": 1,
    "Luis": 8,
    "Marta": 5,
    "Carlos": 3
}

for nombre, nota in notas_alumnos.items():
    if nota >= 5:
        print(f"El alumno {nombre} ha aprobado con una nota de {nota}.")
    else:
        print(f"El alumno {nombre} ha suspendido con una nota de {nota}.")