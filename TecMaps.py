# funcion que imprime los edificios

def mostrar_edificios(edificios):
    i = 1
    print("Edificios disponibles:")
    
    # ciclo que imprime edificio por edificio
    while i <= len(edificios):
        print(i, "-", edificios[i-1])
        i += 1
        
def buscar_edificio(nombre, edificios):
    
    # limpiamos el str del usuario para evitar errores
    nombre = nombre.lower().strip()
    posicion = 0
    # ciclo que recorre los edificios hasta encontrar el ingresado
    while posicion < len(edificios):
        if nombre == edificios[posicion].lower():
            return edificios[posicion]
        posicion += 1
        
    # return en caso de no encontrar ningun edificio
    return ""

def buscar_ruta(inicio, destino, conexiones, edificios):
    
    # convierte el numero de edificio de str a int
    pos_inicio = edificios.index(inicio)
    pos_destino = edificios.index(destino)
    
    # establecemos un booleano para saber hacia donde recorrer la lista
    if pos_destino > pos_inicio:
        direccion  = True
    else:
        direccion = False
        
    ruta = []
    actual = inicio
    
    
    while actual != destino:
        
        # for que recorre toda la lista hasta encontrar el edificio actual
        for i in range(len(conexiones)):
            
            # if cuando el edificio es el index 0
            if conexiones[i][0] == actual:
                
                # establecer siguiente si la lista se recorre hacia arriba
                if direccion:
                    
                    siguiente = conexiones[i][1]
                    instruccion = conexiones[i][2]
                
                # establecer siguiente si la lista se recorre hacia abajo
                elif not direccion:
                    
                    if i > 0:
                        siguiente = conexiones[i-1][0]
                        instruccion = conexiones[i-1][3]
            
            # if cuando el edificio es el index 2
            elif conexiones [i][1] == actual:
                
                # establecer siguiente si la lista se recorre hacia arriba
                if direccion:
                    
                    if i < len(conexiones) - 1:
                        siguiente = conexiones[i+1][1]
                        instruccion = conexiones[i+1][2]
                
                # establecer siguiente si la lista se recorre hacia abajo
                elif not direccion:
                    
                    siguiente = conexiones[i][0]
                    instruccion = conexiones[i][3]
                    
        actual = siguiente
        ruta.append(instruccion)

    return ruta
                    
            

def mostrar_ruta(ruta):
   
   i = 0
   print(ruta[i])
   i += 1
   
   while i < len(ruta):
      siguiente = input("presiona enter para mostrar el siguiente paso")
      
      if siguiente == "":
          print(ruta[i])
          i += 1
   
def main():
    
    #========================= BASE DE DATOS =========================
    
    edificios = [
        "Edificio I",
        "Edificio II",
        "Edificio III",
        "Edificio IV",
        "Edificio V",
        "Edificio VI",
        "Edificio VII",
        "Edificio VIII",
        "Edificio IX",
        "Edificio X",
        ]
    
    conexiones = [
        ["Edificio I", "Edificio II", "Camina hacia el edificio II", "Camina hacia el edificio I"],
        ["Edificio II", "Edificio III", "Camina hacia el edificio III", "Camina hacia el edificio II"],
        ["Edificio III", "Edificio IV", "Camina hacia el edificio IV", "Camina hacia el edificio III"],
        ["Edificio IV", "Edificio V", "Camina hacia el edificio V", "Camina hacia el edificio IV"],
        ["Edificio V", "Edificio VI", "Camina hacia el edificio VI", "Camina hacia el edificio V"],
        ["Edificio VI", "Edificio VII", "Camina hacia el edificio VII", "Camina hacia el edificio VI"],
        ["Edificio VII", "Edificio VIII", "Camina hacia el edificio VIII", "Camina hacia el edificio VII"],
        ["Edificio VIII", "Edificio IX", "Camina hacia el edificio IX", "Camina hacia el edificio VIII"],
        ["Edificio IX", "Edificio X", "Camina hacia el edificio X", "Camina hacia el edificio IX"]
    ]
    
    #========================= BASE DE DATOS =========================
    
    #========================= MENU ========================= 
    print("███████████████████████████████████████████████")
    print("█─▄─▄─█▄─▄▄─█─▄▄▄─███▄─▀█▀─▄██▀▄─██▄─▄▄─█─▄▄▄▄█")
    print("███─████─▄█▀█─███▀████─█▄█─███─▀─███─▄▄▄█▄▄▄▄─█")
    print("▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀▀▀▄▄▄▀▄▄▄▀▄▄▀▄▄▀▄▄▄▀▀▀▄▄▄▄▄▀")
    print("                                               ")
    i = 0
    while True:
        if i > 0:
            print("                                               ")
            print("███████████████████████████████████████████████")
            print("                                               ")
        i += 1
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
                    ruta = buscar_ruta(inicio, destino, conexiones, edificios)
                    mostrar_ruta(ruta)
                    
            case "2":
                
                mostrar_edificios(edificios)
                
            case "3":
                
                print("Programa terminado")
                break
            
            case _:
                
                print("Opcion no valida")
#========================= MENU ========================= 

main()