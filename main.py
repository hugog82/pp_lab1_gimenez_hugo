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
        
mostrar_nombre_y_dato(lista_jugadores, "posicion")

def mostrar_indice_y_nombre (lista:list, dato:str):
    '''
    - Muestra el nombre y el dato pasado por parametro.
    - Recibe una lista, una constante para formatear el print y
      y el dato.
    - No retorna nada.
    '''
    for jugador in lista:
        print("Indice: {0} - Nombre: {1}".format(jugador["nombre"], jugador[dato]))


def obtener_estadisticas_jugador (lista:list, indice:str)->list:
    '''
    - 
    '''
    retorno = None
    if lista != []:
        for jugador in lista:
            