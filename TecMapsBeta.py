def mostrar_edificios(edificios):
    x = 1
    print("Edificios disponibles:")
    while x <= len(edificios):
        print(x, "-", edificios[x-1])
        x += 1

def buscar_edificio(nombre, edificios):
    nombre = nombre.lower().strip()
    posicion = 0
    while posicion < len(edificios):
        if nombre == edificios[posicion].lower():
            return edificios[posicion]
        posicion += 1
    return ""

def buscar_ruta(inicio, destino, conexiones):
    visitados = [inicio]
    pendientes = [[inicio, [[inicio, "Comienza aquí."]]]]
    posicion = 0
    while posicion < len(pendientes):
        actual = pendientes[posicion][0]
        ruta_actual = pendientes[posicion][1]
        posicion += 1
        if actual == destino:
            return ruta_actual
        indice = 0
        while indice < len(conexiones):
            conexion = conexiones[indice]
            if conexion[0] == actual:
                siguiente = conexion[1]
                instruccion = conexion[2]
            elif conexion[1] == actual:
                siguiente = conexion[0]
                instruccion = conexion[3]
            else:
                siguiente = ""
                instruccion = ""
            if siguiente != "":
                if siguiente not in visitados:
                    visitados.append(siguiente)
                    nueva_ruta = ruta_actual + [[siguiente, instruccion]]
                    pendientes.append([siguiente, nueva_ruta])
            indice += 1
    return []
        
def mostrar_ruta(ruta):
    if len(ruta) == 0:
        print("No se encontró ruta")
    else:
        print("=====𝙍𝙪𝙩𝙖=====")
        x = 0
        while x < len(ruta):
            edificio = ruta[x][0]
            instruccion = ruta[x][1]
            if x == 0:
                print("Inicio:", edificio)
            else:
                print("Paso", x, ":")
                print(instruccion)
                print("Llegas a:", edificio)
            x += 1
def main():

#Edificios
    edificios = [
        "Edificio I",
        "Edificio II",
        "Edificio III",
        "Edificio IV",
        "Edificio V",
        "Centro de Bioingeniería",
        "Centro de Medios",
        "Biblioteca",
        "Edificio de Servicios de Apoyo",
        "Centro de Congresos",
        "Centro Estudiantil",
        "Edificio XIV",
        "Centro de Diseño, Innovación y Creación Industrial",
        "Centro de Innovación en Manufactura Avanzada",
        "PrepaTec",
        "Estadio Borregos",
        "Residencias Tec"
    ]
#Conexiones entre edificios
    conexiones = [

        [
            "Edificio I",
            "Edificio II",
            "Camina hacia el Edificio II.",
            "Camina hacia el Edificio I."
        ],

        [
            "Edificio II",
            "Edificio III",
            "Sigue el camino hacia el Edificio III.",
            "Sigue el camino hacia el Edificio II."
        ],

        [
            "Edificio III",
            "Edificio IV",
            "Camina hacia el Edificio IV.",
            "Camina hacia el Edificio III."
        ],

        [
            "Edificio III",
            "Centro de Bioingeniería",
            "Sigue el andador hacia Centro de Bioingeniería.",
            "Regresa por el andador hacia Edificio III."
        ],

        [
            "Centro de Bioingeniería",
            "Edificio V",
            "Camina hacia Edificio V.",
            "Camina hacia Centro de Bioingeniería."
        ],

        [
            "Edificio IV",
            "Centro de Medios",
            "Sigue el camino hacia Centro de Medios.",
            "Regresa hacia Edificio IV."
        ],

        [
            "Centro de Medios",
            "Biblioteca",
            "Camina hacia Biblioteca.",
            "Camina hacia Centro de Medios."
        ],

        [
            "Edificio V",
            "Biblioteca",
            "Sigue el andador hacia Biblioteca.",
            "Sigue el andador hacia Edificio V."
        ],

        [
            "Biblioteca",
            "Edificio de Servicios de Apoyo",
            "Camina hacia Edificio de Servicios de Apoyo.",
            "Camina hacia Biblioteca."
        ],

        [
            "Edificio de Servicios de Apoyo",
            "Centro de Congresos",
            "Sigue el camino hacia Centro de Congresos.",
            "Regresa hacia Edificio de Servicios de Apoyo."
        ],

        [
            "Centro de Congresos",
            "Centro Estudiantil",
            "Camina hacia Centro Estudiantil.",
            "Camina hacia Centro de Congresos."
        ],

        [
            "Centro Estudiantil",
            "Edificio XIV",
            "Sigue el camino hacia Edificio XIV.",
            "Regresa hacia Centro Estudiantil."
        ],

        [
            "Edificio XIV",
            "Centro de Diseño, Innovación y Creación Industrial",
            "Camina hacia DICI.",
            "Regresa hacia Edificio XIV."
        ],

        [
            "Centro de Diseño, Innovación y Creación Industrial",
            "Centro de Innovación en Manufactura Avanzada",
            "Sigue el camino hacia CIMA.",
            "Sigue el camino hacia DICI."
        ],

        [
            "Centro de Innovación en Manufactura Avanzada",
            "PrepaTec",
            "Camina hacia PrepaTec.",
            "Camina hacia CIMA."
        ],

        [
            "Centro de Innovación en Manufactura Avanzada",
            "Estadio Borregos",
            "Sigue el camino hacia el Estadio Borregos.",
            "Regresa hacia CIMA."
        ],

        [
            "Estadio Borregos",
            "Residencias Tec",
            "Camina hacia Residencias Tec.",
            "Camina hacia el Estadio Borregos."
        ]
    ]

#menú inicial
    print("███████████████████████████████████████████████")
    print("█─▄─▄─█▄─▄▄─█─▄▄▄─███▄─▀█▀─▄██▀▄─██▄─▄▄─█─▄▄▄▄█")
    print("███─████─▄█▀█─███▀████─█▄█─███─▀─███─▄▄▄█▄▄▄▄─█")
    print("▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀▀▀▄▄▄▀▄▄▄▀▄▄▀▄▄▀▄▄▄▀▀▀▄▄▄▄▄▀")
    print("                                               ")
    x = 0
    while True:
        if x > 0:
            print("                                               ")
            print("███████████████████████████████████████████████")
            print("                                               ")
        x += 1
        print("1. Buscar una ruta")
        print("2. Ver edificios")
        print("3. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        match opcion:
            
            case "1":
                edificio_partida = input("¿En qué edificio estás? ")
                edificio_destino = input("¿A qué edificio quieres ir? ")
                inicio = buscar_edificio(edificio_partida, edificios)
                destino = buscar_edificio(edificio_destino, edificios)
                
                if inicio == "":
                    print("El edificio donde estás no existe.")
                elif destino == "":
                    print("El edificio de destino no existe.")
                elif inicio == destino:
                    print("Ya estás en ese edificio.")     
                else:
                    ruta = buscar_ruta(inicio, destino, conexiones)
                    mostrar_ruta(ruta)
                    
            case "2":
                mostrar_edificios(edificios)
                
            case "3":
                print("Programa terminado.")
                break
            
            case _:
                print("Opción no válida.")
    
main()