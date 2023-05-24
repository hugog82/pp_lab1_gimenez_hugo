import json, re

def leer_archivo_json (nombre_archivo:str)->list:
    '''
    - Lee un arhivo de tipo json.
    - Recibe una cadena con la extension json por parametro.
    - Retorna la lista que contiene el archivo.
    - Retorna -1 si la lista esta vacia o el path es incorrecto.
    - Retorna -2 si la extension es incorrecta.
    '''
    retorno = -1
    
    try:
        lista= []
        with open(nombre_archivo, "r") as archivo:
            dict = json.load(archivo)
            lista = dict["jugadores"]
            retorno = lista
    except FileNotFoundError as error_archivo_no_encontrado:
        print(error_archivo_no_encontrado)
        retorno
    except json.JSONDecodeError:
        retorno = -2
        
    return retorno

lista_jugadores = leer_archivo_json("./pp_lab1_gimenez_hugo/dt.json")


def mostrar_nombre_y_dato(lista:list, dato:str):
    '''
    - Muestra el nombre y el dato pasado por parametro.
    - Recibe una lista, una constante para formatear el print y
      y el dato.
    - No retorna nada.
    '''
    for jugador in lista:
        print("Nombre: {0} - Posicion: {1}".format(jugador["nombre"], jugador[dato]))
        
#mostrar_nombre_y_dato(lista_jugadores, "posicion")

def mostrar_indice_y_nombre (lista:list)->bool:
    '''
    - Muestra un numero correspondiente al indice y el nombre del jugador.
    - Recibe una lista.
    - Retorna False si la lista esta vacia sino retorna True.
    '''
    retorno = False
       
    if lista != []:
        for indice in range(len(lista)):
            print("Indice: {0} - Nombre: {1}".format(indice, lista[indice]["nombre"]))
        
        retorno = True
        
    return retorno
    
    
#mostrar_indice_y_nombre(lista_jugadores)

def mostrar_nombre_un_jugador (lista:list, indice:str):
    '''
    - Muestra el nombre de un jugador.
    - Recibe una lista y el indice de la lista.
    - Retorna False si la lista esta vacia sino retorna True.
    '''
    retorno = False
    indice = int(indice)
       
    if lista != []:
        print("Nombre: {0}".format(lista[indice]["nombre"]))
        retorno = True
    return retorno
    

def mostrar_estadisticas_jugador (lista:list, indice:str)->bool:
    '''
    - Muestra las estadisticas de un jugador.
    - Recibe una lista y el indice del jugador a mostrar.
    - Retorna False si la lista esta vacia sino retorna True.
    '''
    retorno = False
    indice = int(indice)
    jugador = lista[indice]
    
    if lista != []:
        for clave in jugador["estadisticas"].keys():
            print("{0} - {1}".format(clave, jugador["estadisticas"][clave]).capitalize(),end="\n")
        
        retorno = True
        
    return retorno


mostrar_nombre_un_jugador(lista_jugadores, "0")
mostrar_estadisticas_jugador (lista_jugadores, "0")