# mostrar lista de edificios

def mostrar_edificios(edificios):
    x = 1
    print("Edificios disponibles:")
    while x <= len(edificios):
        print(x, "-", edificios[x-1])
        x += 1

# comprobar que el edificio existe

def buscar_edificio(nombre, edificios):
    nombre = nombre.lower().strip()
    posicion = 0
    while posicion < len(edificios):
        if nombre == edificios[posicion].lower():
            return edificios[posicion]
        posicion += 1
    return ""
    
# def dolor_de_cabeza()

def buscar_ruta(inicio, destino, conexiones):
    visitados = [inicio]
    pendientes = [[inicio, [[inicio, ""]]]]
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

#imprimir ruta

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

#lista edificios
    
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
            "Camina hacia el Edificio III.",
            "Camina hacia el Edificio II."
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
            "Camina hacia el Centro de Bioingeniería.",
            "Camina hacia el Edificio III."
        ],

        [
            "Centro de Bioingeniería",
            "Edificio V",
            "Camina hacia el Edificio V.",
            "Camina hacia el Centro de Bioingeniería."
        ],

        [
            "Edificio IV",
            "Centro de Medios",
            "Camina hacia el Centro de Medios.",
            "Camina hacia el Edificio IV."
        ],

        [
            "Centro de Medios",
            "Biblioteca",
            "Camina hacia la Biblioteca.",
            "Camina hacia el Centro de Medios."
        ],

        [
            "Edificio V",
            "Biblioteca",
            "Camina hacia la Biblioteca.",
            "Camina hacia el Edificio V."
        ],

        [
            "Biblioteca",
            "Edificio de Servicios de Apoyo",
            "Camina hacia el Edificio de Servicios de Apoyo.",
            "Camina hacia la Biblioteca."
        ],

        [
            "Edificio de Servicios de Apoyo",
            "Centro de Congresos",
            "Camina hacia el Centro de Congresos.",
            "Camina hacia el Edificio de Servicios de Apoyo."
        ],

        [
            "Centro de Congresos",
            "Centro Estudiantil",
            "Camina hacia el Centro Estudiantil.",
            "Camina hacia el Centro de Congresos."
        ],

        [
            "Centro Estudiantil",
            "Edificio XIV",
            "Camina hacia el Edificio XIV.",
            "Camina hacia el Centro Estudiantil."
        ],

        [
            "Edificio XIV",
            "Centro de Diseño, Innovación y Creación Industrial",
            "Camina hacia el DICI.",
            "Camina hacia el Edificio XIV."
        ],

        [
            "Centro de Diseño, Innovación y Creación Industrial",
            "Centro de Innovación en Manufactura Avanzada",
            "Camina hacia el CIMA.",
            "Camina hacia el DICI."
        ],

        [
            "Centro de Innovación en Manufactura Avanzada",
            "PrepaTec",
            "Camina hacia PrepaTec.",
            "Camina hacia el CIMA."
        ],

        [
            "Centro de Innovación en Manufactura Avanzada",
            "Estadio Borregos",
            "Camina hacia el Estadio Borregos.",
            "Camina hacia el CIMA."
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
