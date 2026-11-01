# TecMAPS 🗺️

## Descripción del proyecto

**TecMAPS** es un programa desarrollado en Python que permite a los estudiantes y visitantes consultar los edificios disponibles dentro del campus y obtener instrucciones para desplazarse de un edificio a otro.

El proyecto busca facilitar la orientación dentro del campus mediante un sistema sencillo de búsqueda de rutas.

## Funcionalidades

- **Buscar una ruta:** permite seleccionar un edificio de partida y uno de destino para obtener las instrucciones de recorrido.
- **Ver edificios:** muestra la lista de edificios disponibles.
- **Validación de entradas:** comprueba que los edificios ingresados existan y que la opción seleccionada en el menú sea válida.
- **Instrucciones paso a paso:** muestra las indicaciones de la ruta una por una, permitiendo avanzar con la tecla Enter.


## Organización del programa

El programa está dividido en las siguientes funciones:

| Función | Descripción |
|---|---|
| `mostrar_edificios()` | Muestra los edificios disponibles. |
| `buscar_edificio()` | Busca y valida el nombre de un edificio. |
| `buscar_ruta()` | Calcula la secuencia de conexiones entre el edificio inicial y el destino. |
| `mostrar_ruta()` | Presenta las instrucciones de recorrido paso a paso. |
| `main()` | Contiene la base de datos y controla el menú principal. |

## ¿Cómo utilizarlo?

1. Ejecutar el archivo principal de Python.
2. Seleccionar una opción del menú:
   - `1`: Buscar una ruta.
   - `2`: Ver edificios disponibles.
   - `3`: Salir del programa.
3. Si se selecciona la opción de búsqueda, ingresar el edificio de partida y el edificio de destino.
4. Presionar Enter para avanzar entre las instrucciones de la ruta.

**NOTA IMPORTANTE:**

La base de datos contiene con edificios falsos, el campus aún no esta mapeado
