# Sistema de Inscripción a Cursos

## Descripción

Este proyecto consiste en un sistema de gestión de inscripciones a cursos desarrollado en Python. Permite registrar estudiantes, administrar cursos, gestionar inscripciones respetando el cupo disponible, crear listas de espera y mostrar estadísticas generales del sistema.

# Uso de IA

En este proyecto utilizamos la IA para responder dudas en cuanto a la implementación de archivos de tipo .txt en el cual evidenciamos un trabajo terminado prolijo y conforme a las consignas planteadas para el proyecto.
Con la IA también trabajamos para generar algunas ideas en las funciones que posteriormente implementamos en el código.

## Funcionalidades

- Registrar estudiantes.
- Visualizar estudiantes registrados.
- Crear cursos.
- Visualizar cursos disponibles.
- Inscribir estudiantes en cursos.
- Gestionar listas de espera cuando un curso alcanza su cupo máximo.
- Mostrar estadísticas generales del sistema.

## Estructura de archivos

- `main.py`: Contiene la lógica principal del programa.
- `estudiantes.txt`: Almacena los datos de los estudiantes.
- `cursos.txt`: Almacena la información de los cursos.
- `inscripciones.txt`: Guarda las inscripciones y el estado de cada estudiante (INSCRIPTO o ESPERA).

## Requisitos

- Python 3.10 o superior.

## Ejecución

1. Clonar el repositorio.
2. Abrir la carpeta del proyecto.
3. Ejecutar:

```bash
python main.py
```

## -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Funciones principales

## inicializar_archivos()

Esta función verifica si existen los archivos estudiantes.txt, cursos.txt e inscripciones.txt. En caso de que alguno no exista, lo crea automáticamente para que el sistema pueda almacenar la información sin generar errores al ejecutarse por primera vez.

## buscar_curso(id_buscar)

Busca un curso dentro del archivo cursos.txt utilizando su ID. Si encuentra el curso, devuelve toda su información; en caso contrario, devuelve None.

# buscar_estudiante(dni_buscar)

Busca un estudiante en el archivo estudiantes.txt a partir de su DNI. Si el estudiante existe, retorna sus datos; si no, devuelve None.

# ya_inscripto(dni, id_curso)

Verifica si un estudiante ya se encuentra inscripto en un determinado curso consultando el archivo inscripciones.txt. Devuelve True si ya está registrado y False en caso contrario.

# cantidad_inscriptos(id_curso)

Cuenta la cantidad de estudiantes que se encuentran inscriptos en un curso determinado. Recorre el archivo inscripciones.txt y devuelve únicamente los alumnos cuyo estado es INSCRIPTO, sin contar a los que están en lista de espera.

# dni_existe(dni_buscar)

Verifica si un DNI ya se encuentra registrado en el sistema. Esta validación evita que un mismo estudiante pueda registrarse más de una vez.

# curso_existe(nombre_buscar)

Comprueba si un curso ya fue creado previamente. La comparación se realiza sin distinguir entre mayúsculas y minúsculas para evitar cursos duplicados con nombres escritos de forma diferente.

# obtener_siguiente_id()

Obtiene el próximo ID disponible para un nuevo curso. Para ello, recorre el archivo cursos.txt, identifica el último ID registrado y devuelve ese valor incrementado en uno.

# registrar_estudiante()

Permite registrar un nuevo estudiante solicitando su nombre, DNI y correo electrónico. Antes de guardar la información, valida que el nombre no esté vacío, que el DNI sea numérico y que no se encuentre previamente registrado. Finalmente, almacena los datos en el archivo estudiantes.txt.

# ver_estudiantes()

Muestra por pantalla la lista de todos los estudiantes registrados en el sistema. La información se obtiene del archivo estudiantes.txt y se presenta de forma ordenada con un número de registro, DNI, nombre y correo electrónico. Si no existen estudiantes registrados, informa esta situación al usuario.

# crear_curso()

Permite registrar un nuevo curso en el sistema. Solicita el nombre del curso y la cantidad máxima de alumnos, valida que el nombre no esté vacío, que el cupo sea mayor a cero y que el curso no exista previamente. Luego asigna un ID único y guarda la información en el archivo cursos.txt.

# ver_lista_espera()

Muestra todos los estudiantes que se encuentran en lista de espera. Para cada registro, recupera los datos del estudiante y del curso correspondiente, mostrando el nombre del alumno, su DNI y el curso al que espera ingresar. Si no existen estudiantes en espera, informa esta situación al usuario.

# inscribir_estudiante()

Permite inscribir un estudiante en un curso. Primero verifica que el estudiante y el curso existan y que el alumno no esté previamente inscripto. Luego comprueba si el curso tiene cupos disponibles: si los hay, registra la inscripción como INSCRIPTO; en caso contrario, el estudiante es agregado automáticamente a la LISTA DE ESPERA. Finalmente, la inscripción se almacena en el archivo inscripciones.txt.

# ver_cursos()

Muestra todos los cursos registrados en el sistema. Para cada curso se visualiza su ID, nombre, cupo máximo, cantidad de estudiantes inscriptos y lugares disponibles. Si no existen cursos registrados, informa esta situación al usuario.

# mostrar_estadisticas()

Genera un resumen general del sistema a partir de la información almacenada en los archivos de datos. Calcula el total de estudiantes registrados, la cantidad de cursos disponibles, el número de inscripciones realizadas, los estudiantes en lista de espera y determina cuál es el curso con mayor cantidad de inscriptos.

### Alumnos:

Campos Basualdo Evelin - Legajo: 23490.
Barreto Yamila Elisa - Legajo: 31168.
Vaz Maria Luna - Legajo: 29226.
Richter, Carlos Nicolas Augusto - Legajo: 26785
