import os

ARCHIVO_ESTUDIANTES = "estudiantes.txt"
ARCHIVO_CURSOS = "cursos.txt"
ARCHIVO_INSCRIPCIONES = "inscripciones.txt"


def inicializar_archivos():

    if not os.path.exists(ARCHIVO_ESTUDIANTES):
        open(ARCHIVO_ESTUDIANTES, "w", encoding="utf-8").close()

    if not os.path.exists(ARCHIVO_CURSOS):
        open(ARCHIVO_CURSOS, "w", encoding="utf-8").close()

    if not os.path.exists(ARCHIVO_INSCRIPCIONES):
        open(ARCHIVO_INSCRIPCIONES, "w", encoding="utf-8").close()


def mostrar_menu():
    print("\n" + "=" * 40)
    print(" SISTEMA DE INSCRIPCIÓN A CURSOS ")
    print("=" * 40)
    print("1. Registrar estudiante")
    print("2. Ver estudiantes")
    print("3. Crear curso")
    print("4. Ver cursos")
    print("5. Inscribir estudiante")
    print("6. Ver lista de espera")
    print("7. Estadísticas")
    print("8. Salir")
    print("=" * 40)

def buscar_curso(id_buscar):

    with open(ARCHIVO_CURSOS, "r", encoding="utf-8") as archivo:

        for linea in archivo:

            datos = linea.strip().split(";")

            if len(datos) == 3:

                if datos[0] == id_buscar:
                    return datos

    return None

def buscar_estudiante(dni_buscar):

    with open(ARCHIVO_ESTUDIANTES, "r", encoding="utf-8") as archivo:

        for linea in archivo:

            datos = linea.strip().split(";")

            if len(datos) == 3:

                if datos[0] == dni_buscar:
                    return datos

    return None

def ya_inscripto(dni, id_curso):

    with open(ARCHIVO_INSCRIPCIONES, "r", encoding="utf-8") as archivo:

        for linea in archivo:

            datos = linea.strip().split(";")

            if len(datos) == 3:

                if datos[0] == dni and datos[1] == id_curso:
                    return True

    return False

def cantidad_inscriptos(id_curso):

    contador = 0

    with open(ARCHIVO_INSCRIPCIONES, "r", encoding="utf-8") as archivo:

        for linea in archivo:

            datos = linea.strip().split(";")

            if len(datos) == 3:

                if datos[1] == id_curso and datos[2] == "INSCRIPTO":
                    contador += 1

    return contador

def dni_existe(dni_buscar):
    with open(ARCHIVO_ESTUDIANTES, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            datos = linea.strip().split(";")

            if len(datos) == 3:
                dni = datos[0]

                if dni == dni_buscar:
                    return True

    return False

def curso_existe(nombre_buscar):

    with open(ARCHIVO_CURSOS, "r", encoding="utf-8") as archivo:

        for linea in archivo:

            datos = linea.strip().split(";")

            if len(datos) == 3:

                nombre = datos[1]

                if nombre.lower() == nombre_buscar.lower():
                    return True

    return False

def obtener_siguiente_id():

    ultimo_id = 0

    with open(ARCHIVO_CURSOS, "r", encoding="utf-8") as archivo:

        for linea in archivo:

            datos = linea.strip().split(";")

            if len(datos) == 3:

                ultimo_id = int(datos[0])

    return ultimo_id + 1


def registrar_estudiante():
    print("\n===== REGISTRAR ESTUDIANTE =====")

    nombre = input("Nombre: ").strip()

    while nombre == "":
        print("El nombre no puede estar vacío.")
        nombre = input("Nombre: ").strip()

    dni = input("DNI: ").strip()

    while not dni.isdigit():
        print("El DNI solo puede contener números.")
        dni = input("DNI: ").strip()

    if dni_existe(dni):
        print("\nEse DNI ya está registrado.")
        return

    email = input("Email: ").strip()

    with open(ARCHIVO_ESTUDIANTES, "a", encoding="utf-8") as archivo:
        archivo.write(f"{dni};{nombre};{email}\n")

    print("\nEstudiante registrado correctamente.")


def ver_estudiantes():
    print("\n===== LISTA DE ESTUDIANTES =====")

    with open(ARCHIVO_ESTUDIANTES, "r", encoding="utf-8") as archivo:

        contador = 0

        for linea in archivo:
            datos = linea.strip().split(";")

            if len(datos) == 3:
                contador += 1

                dni = datos[0]
                nombre = datos[1]
                email = datos[2]

                print(f"\nEstudiante {contador}")
                print(f"DNI: {dni}")
                print(f"Nombre: {nombre}")
                print(f"Email: {email}")

        if contador == 0:
            print("No hay estudiantes registrados.")

def crear_curso():

    print("\n===== CREAR CURSO =====")

    nombre = input("Nombre del curso: ").strip()

    while nombre == "":
        print("El nombre no puede estar vacío.")
        nombre = input("Nombre del curso: ").strip()

    if curso_existe(nombre):
        print("Ese curso ya existe.")
        return

    while True:

        try:
            cupo = int(input("Cantidad máxima de alumnos: "))

            if cupo > 0:
                break

            print("El cupo debe ser mayor que cero.")

        except ValueError:
            print("Debe ingresar un número.")

    id_curso = obtener_siguiente_id()

    with open(ARCHIVO_CURSOS, "a", encoding="utf-8") as archivo:
        archivo.write(f"{id_curso};{nombre};{cupo}\n")

    print("\nCurso registrado correctamente.")


def ver_lista_espera():

    print("\n===== LISTA DE ESPERA =====")

    hay_espera = False

    with open(ARCHIVO_INSCRIPCIONES, "r", encoding="utf-8") as archivo:

        for linea in archivo:

            datos = linea.strip().split(";")

            if len(datos) == 3:

                if datos[2] == "ESPERA":

                    estudiante = buscar_estudiante(datos[0])
                    curso = buscar_curso(datos[1])

                    print("-----------------------------")
                    print("Alumno:", estudiante[1])
                    print("DNI:", estudiante[0])
                    print("Curso:", curso[1])

                    hay_espera = True

    if not hay_espera:
        print("No hay estudiantes en lista de espera.")


def inscribir_estudiante():

    print("\n===== INSCRIPCIÓN =====")

    dni = input("Ingrese el DNI del estudiante: ")

    estudiante = buscar_estudiante(dni)

    if estudiante is None:
        print("El estudiante no existe.")
        return

    ver_cursos()

    id_curso = input("\nIngrese el ID del curso: ")

    curso = buscar_curso(id_curso)

    if curso is None:
        print("Ese curso no existe.")
        return

    if ya_inscripto(dni, id_curso):
        print("El estudiante ya está anotado en este curso.")
        return

    cupo = int(curso[2])

    inscriptos = cantidad_inscriptos(id_curso)

    if inscriptos < cupo:
        estado = "INSCRIPTO"
        print("Inscripción realizada correctamente.")
    else:
        estado = "ESPERA"
        print("No quedan cupos.")
        print("El estudiante fue agregado a la lista de espera.")

    with open(ARCHIVO_INSCRIPCIONES, "a", encoding="utf-8") as archivo:
        archivo.write(f"{dni};{id_curso};{estado}\n")


def ver_cursos():

    print("\n===== CURSOS DISPONIBLES =====")

    contador = 0

    with open(ARCHIVO_CURSOS, "r", encoding="utf-8") as archivo:

        for linea in archivo:

            datos = linea.strip().split(";")

            if len(datos) == 3:

                contador += 1

                id_curso = datos[0]
                nombre = datos[1]
                cupo = int(datos[2])

                inscriptos = cantidad_inscriptos(id_curso)
                disponibles = cupo - inscriptos

                print(f"\nCurso {contador}")
                print(f"ID: {id_curso}")
                print(f"Nombre: {nombre}")
                print(f"Cupo máximo: {cupo}")
                print(f"Inscriptos: {inscriptos}")
                print(f"Lugares disponibles: {disponibles}")

    if contador == 0:
        print("No hay cursos registrados.")
    
def mostrar_estadisticas():

    print("\n===== ESTADÍSTICAS =====")

    # Total de estudiantes
    total_estudiantes = 0
    with open(ARCHIVO_ESTUDIANTES, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            if linea.strip():
                total_estudiantes += 1

    # Total de cursos
    total_cursos = 0
    with open(ARCHIVO_CURSOS, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            if linea.strip():
                total_cursos += 1

    # Total de inscriptos y lista de espera
    total_inscriptos = 0
    total_espera = 0

    with open(ARCHIVO_INSCRIPCIONES, "r", encoding="utf-8") as archivo:
        for linea in archivo:

            datos = linea.strip().split(";")

            if len(datos) == 3:

                if datos[2] == "INSCRIPTO":
                    total_inscriptos += 1

                elif datos[2] == "ESPERA":
                    total_espera += 1

    # Curso con mayor cantidad de inscriptos
    nombre_curso = "Ninguno"
    mayor = -1

    with open(ARCHIVO_CURSOS, "r", encoding="utf-8") as archivo:

        for linea in archivo:

            datos = linea.strip().split(";")

            if len(datos) == 3:

                cantidad = cantidad_inscriptos(datos[0])

                if cantidad > mayor:
                    mayor = cantidad
                    nombre_curso = datos[1]

    print("\n===== RESUMEN =====")
    print(f"Total de estudiantes: {total_estudiantes}")
    print(f"Total de cursos: {total_cursos}")
    print(f"Total de inscripciones: {total_inscriptos}")
    print(f"Estudiantes en lista de espera: {total_espera}")
    print(f"Curso con más inscriptos: {nombre_curso} ({mayor} alumnos)")

def main():

    inicializar_archivos()

    while True:

        mostrar_menu()

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Debe ingresar un número.")
            continue

        match opcion:

            case 1:
                registrar_estudiante()

            case 2:
                ver_estudiantes()

            case 3:
                    crear_curso()

            case 4:
                    ver_cursos()

            case 5:
                inscribir_estudiante()

            case 6:
                ver_lista_espera()

            case 7:
                mostrar_estadisticas()

            case 8:
                print("\nGracias por utilizar el sistema.")
                break

            case _:
                print("\nOpción inválida.")

# Menú principal
main()