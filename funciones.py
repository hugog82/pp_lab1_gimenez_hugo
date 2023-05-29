import json, re

def es_entero (cadena:str)->None:
    '''
    - Busca numeros enteros dentro de una cadena.
    - Obtiene una cadena por parametro.
    - Retorna la cadena si hay solo numeros en la cadena.
    - Retorna None si la cadena esta vacia 
      o si hay algun caracter que no sea un numero.
    '''
    retorno = None
    respuesta = re.match(r'^-[0-9]|^[0-9]+$', cadena)
    
    if cadena != "" and respuesta != None:
        retorno = respuesta.group()
    
    return retorno

def es_solo_texto (cadena:str)->bool:
    '''
    - Busca palabras donde todos sus caracteres sean alfabeticos.
    - Obtiene una cadena por parametro.
    - Retorna True si encuentra alguna palabra.
      o False si no encuentra ninguna palabra o la cadena esta vacia.
    '''
    retorno = False
    respuesta = re.search(r'^[a-zA-Z ]+$', cadena)

    if cadena == "" or respuesta == None:
        retorno
    else:
        retorno = True

    return retorno

def imprimir_dato(variable:str):
    '''
    - Imprime por consola la variable recibida.
    - Recibe una variable del tipo string.
    - No retorna nada.
    '''
    print(variable)

def leer_archivo_json (nombre_archivo:str)->list:
    '''
    - Lee un arhivo de tipo json.
    - Recibe un path del tipo str con la extension json por parametro.
    - Retorna la lista que contiene el archivo.
    - Retorna None si el str esta vacio.
    '''
    retorno = None
    
    if nombre_archivo != "":
        with open (nombre_archivo, "r") as archivo:
            dict = json.load(archivo)
            lista = dict["jugadores"]
            retorno = lista

    return retorno

def mostrar_nombres_y_datos(lista:list, constante, dato:str)->bool:
    '''
    - Muestra una lista de nombre y datos.
    - Recibe por parametro una lista, una constante para formatear el
      print y el dato.
    - Si la lista esta vacia retorna False.
    '''
    retorno = False
    if lista != []:
        for jugador in lista:
            print("Nombre: {0} - {1}: {2}".format(jugador["nombre"], constante, jugador[dato]))
            retorno = True 
    return retorno

def mostrar_indice_y_nombre (lista:list)->bool:
    '''
    - Muestra un numero correspondiente al indice y el nombre del jugador.
    - Recibe una lista.
    - Retorna False si la lista esta vacia sino retorna True.
    '''
    retorno = False
       
    if lista != []:
        for indice in range(len(lista)):
            print("Indice: {0} - Nombre: {1}".format(indice+1, lista[indice]["nombre"]))
        retorno = True
        
    return retorno
        
def mostrar_un_jugador_nombre_dato (lista:list, indice:str, dato:str)->bool:
    '''
    - Muestra el nombre de un jugador.
    - Recibe una lista ,el indice de la lista y un dato, pj: 'posicion'
    - Retorna False si la lista esta vacia sino retorna True.
    '''
    retorno = False
    indice = int(indice)
       
    if lista != []:
        print("Nombre: {0} \nPosicion: ".format(lista[indice]["nombre"]),lista[indice][dato])
        retorno = True
    return retorno
    
def mostrar_estadisticas_jugador (lista:list, indice:str)->dict:
    '''
    - Muestra las estadisticas de un jugador.
    - Recibe una lista y el indice del jugador a mostrar.
    - Retorna False si la lista esta vacia sino retorna True.
    '''
    retorno = False
    indice = int(indice)
    jugador = lista[indice]
    
    if lista != []:
        print("Nombre: {}".format(jugador["nombre"]))
        for clave in jugador["estadisticas"].keys():
            print("{0} - {1}".format(clave, jugador["estadisticas"][clave]).capitalize(),end="\n")
        
        retorno = jugador
        
    return retorno

def formatear_nombre_a_guardar(jugador:dict)->str:
    '''
    - Da formato al string tomando el nombre del jugador para guardar en un csv.
    - Recibe un jugador por parametro.
    - Retorna un string para el nombre del csv.
    '''
    nombre = jugador["nombre"].replace(" ", "_")
    nombre_a_guardar = "./pp_lab1_gimenez_hugo/estadistica_{}.csv".format(nombre)
    return nombre_a_guardar

def parser_csv(jugador:dict)->str:
    '''
    - Convierte una lista a un string con los valores separados por comas.
    - Recibe por parametro una lista.
    - Retorna la cabecera y los elementos de la lista.
    - Retorna None si la lista esta vacia.
    ''' 
    retorno = None
    
    if jugador != {}:
        lista_cabecera = []    
        
        for valor_cabecera in jugador.keys():
            if valor_cabecera != "estadisticas" and valor_cabecera != "logros":
                lista_cabecera.append(valor_cabecera)
        for valor_cabecera in jugador["estadisticas"].keys():
            lista_cabecera.append(valor_cabecera)
        cabecera = ""
        cabecera += ",".join(lista_cabecera)
        cabecera += "\n"

        lista_datos = []
        
        for valor_dato in jugador.values():
            if valor_dato != jugador["estadisticas"] and valor_dato != jugador["logros"]:
                lista_datos.append(valor_dato)
        for valor_dato in jugador["estadisticas"].values():
            if valor_dato != jugador["logros"]:
                if type(valor_dato) is not str:
                    valor_dato = str(valor_dato)
                    lista_datos.append(valor_dato)
        datos = ""
        datos += ",".join(lista_datos)
        datos += "\n"
        retorno = cabecera + datos
        
    return retorno
        
def guardar_archivo(nombre_archivo:str,contenido:str)->int:
    '''
    - Guarda un archivo en formato csv.
    - Recibe por parametro el nombre con el que se va a guardar
      y el contenido a guardar.
    - Compara el retorno del metodo write y lo compara con el len
      del contenido. Si son igual muestra un mensaje de exito.
    - En caso de no coincidir muestra un mensaje de error.
    - Si el objeto contenido esta vacio retorna -1, sino retorna 0.
    '''
    retorno = -1
    if contenido != "":    
        with open(nombre_archivo,"w") as archivo:
            valor = archivo.write(contenido)
            if valor == len(contenido):
                print("El archivo se guardo correctamente!")
            else:
                print("ERROR: No se pudo guardar el archivo!")
        retorno = 0
        
    return retorno

def obtener_logros_jugador(jugadores:list, nombre:str)->list:
    '''
    - Obtiene los logros de un judador.
    - Recibe como parametro una lista de jugadores y el nombre a buscar.
    - Retorna una nueva lista con el nombre y los logros.
    - Si esta vacia retorna None.
    '''
    retorno = None
    nueva_lista = []
    
    if jugadores != []:
        for jugador in jugadores:
            if re.search(nombre, jugador["nombre"], re.I) != None:
                nueva_lista.append(jugador["nombre"])
                nueva_lista.extend(jugador["logros"])
                retorno = nueva_lista
            
    return retorno

def mostrar_logros_jugador (jugador:dict)->bool:
    '''
    - Muestra los logros de un jugador.
    - Recibe un diccionario.
    - Retorna False si la lista esta vacia sino retorna True.
    '''
    retorno = False
        
    if jugador != {}:
        print("Nombre: {}".format(jugador[0]))
        print("Logros:")
        for valor in jugador[1:]:
            print("\t{0}".format(valor,end="\n"))
        
        retorno = jugador
        
    return retorno

def sumar_dato_jugador (lista:list, dato:str)->float:
    '''
    - Suma los datos obtenidos por parametro.
    - Recibe una lista y un dato a sumar.
    - Si la lista esta vacia retorna None sino retorna la suma.
    '''
    retorno = None
    suma = 0
    
    if lista != []:
        for jugador in lista:
            for valor in jugador["estadisticas"]:
                if valor == dato:
                    puntos = jugador["estadisticas"][valor]
                    suma += puntos
                    retorno = suma            
    return retorno

def dividir(dividendo:int, divisor:int):
    '''
    - Divide dos numeros recibidos por parametro.
    - Recibe un dividendo y un divisor.
    - Retorna la division entre los parametros.
    - Si el divisor es igual a 0 retorna 0.
    '''
    retorno = divisor

    if divisor != 0:
        resultado = dividendo / divisor
        retorno = resultado
    
    return retorno
 
def obtener_promedio_puntos_partidos_del_equipo (lista:list, dato:str)->float:
    ''' 
    - Calcula el promedio del dato recibido en la lista.
    - Recibe como parametros una lista y el dato a calcular.
    - Retorna el promedio calculado.
    - Si la lista esta vacia retorna None.
    '''
    retorno = None

    if lista != []:
        suma = sumar_dato_jugador(lista, dato)
        cantidad = len(lista)
        promedio = dividir(suma, cantidad)
        retorno = promedio
    
    return retorno

def ordenar_por_key (lista_jugadores:list, dato:str, orden:bool=True)->list:
    '''
    - Ordena la lista segun el dato/key de forma ascendente o descendente.
    - Recibe una lista por parametro, el dato a ordenar y el tipo de orden.
    - True = Ascendente o False = Descendente.
    - Retorna la lista ordenada.
    - Si la lista esta vacia retorna None.
    '''
    retorno = None
    
    if lista_jugadores != []:
        if len(lista_jugadores) > 1:
            rango_a = len(lista_jugadores)
            flag_swap = True

            while(flag_swap):
                flag_swap = False
                rango_a = rango_a - 1

                for indice_a in range(rango_a):
                    if  orden == False and lista_jugadores[indice_a][dato] < lista_jugadores[indice_a+1][dato] \
                    or orden == True and lista_jugadores[indice_a][dato] > lista_jugadores[indice_a+1][dato]:
                        lista_jugadores[indice_a],lista_jugadores[indice_a+1] = lista_jugadores[indice_a+1],lista_jugadores[indice_a]
                        flag_swap = True
        retorno = lista_jugadores
        
    return retorno


def es_miembro_salon_de_la_fama (lista_jugadores:list, nombre:str)->bool:
    '''
    - Evalua si el jugador buscado es miembro del salon de la fama.
    - Recibe una lista de jugadores y el nombre a evaluar.
    - Retorna None si la lista esta vacia. False si no es miembro y
      True si es miembro.
    '''
    retorno = None
    
    if lista_jugadores != []:
        retorno = False
        for jugador in lista_jugadores:
            if re.search(nombre, jugador["nombre"], re.I) != None:
                for valor in jugador["logros"]:
                    if re.search("miembro", valor, re.I) != None:
                        retorno = True
    return retorno

def obtener_jugador_mayor_dato (lista_jugadores:list, dato:str)->dict:
    '''
    - Obtiene el jugador con el mayor valor segun el dato obtenido
      por parametro.
    - Recibe una lista y un dato a evaluar.
    - Retorna None si la lista esta vacia sino retorna un jugador.
    '''
    retorno = None
    mayor_dato = 0
        
    if lista_jugadores != []:
        for jugador in lista_jugadores:
            for valor in jugador["estadisticas"]:
                if valor == dato and jugador["estadisticas"][valor] > mayor_dato:
                        mayor_dato = jugador["estadisticas"][valor]
                        retorno = jugador
        return retorno
    
def mostrar_jugador_nombre_dato (jugador:dict, constante:str, dato:str)->bool:
    '''
    - Muestra el nombre y el dato de un jugador.
    - Recibe por parametro una jugador, una constante para formatear el
      print y el dato.
    - Si la lista esta vacia retorna False sino retorna True.  
    '''
    retorno = False
    if jugador != {}:
        print("Nombre: {0} - {1}: {2}".format(jugador["nombre"], constante, jugador["estadisticas"][dato]))
        retorno = True
    return retorno
           
def obtener_mayores (lista_jugadores:list, estadistica:str, numero:str)->list:
    '''
    - Obtiene una lista de jugadores donde se evalua que la estadistica
      sea mayor al numero ingresado por el usuario.
    - Obtiene por parametro una lista, la estadistica a evaluar y el numero
      ingresado por el usuario.
    - Si la lista esta vacia retorna None. Caso contrario retorna una lista
      con los jugadores que cumplan con los datos evaluados.
    '''
    retorno = None
    nueva_lista = []
    numero = float(numero)
    
    if lista_jugadores != []:
        for jugador in lista_jugadores:
            for valor in jugador["estadisticas"]:
                if valor == estadistica and jugador["estadisticas"][valor] > numero:
                    nueva_lista.append(jugador)
                    retorno = nueva_lista
    return retorno

def mostrar_nombre_y_dato_jugadores (lista:list, constante, dato:str)->bool:
    '''
    - Muestra el nombre y el dato pasado por parametro.
    - Recibe una lista, una constante para formatear el print y
      y el dato.
    - No retorna nada.
    '''
    for jugador in lista:
        print("Nombre: {0} - {1}: {2}".format(jugador["nombre"], constante, jugador["estadisticas"][dato]))
        
def obtener_jugador_menores_puntos_por_partido (lista_jugadores:list)->dict:
    '''
    - Obtiene el jugador con menos puntos por partido.
    - Recibe un lista de jugadores.
    - Retorna None si la lista esta vacia sino retorna un jugador.
    '''
    retorno = None
    menor_dato = 0
    flag_primer_jugador = True    
        
    if lista_jugadores != []:
        for jugador in lista_jugadores:
            for valor in jugador["estadisticas"]:
                if valor == "promedio_puntos_por_partido" and flag_primer_jugador == True:
                    flag_primer_jugador = False
                    menor_dato = jugador["estadisticas"]["promedio_puntos_por_partido"]
                elif valor == "promedio_puntos_por_partido" and jugador["estadisticas"]["promedio_puntos_por_partido"] < menor_dato:
                    menor_dato = jugador["estadisticas"]["promedio_puntos_por_partido"]
                    retorno = jugador
    return retorno


def obtener_mejores_promedios (lista_jugadores:list, jugador_menos_puntos:dict)->list:
    '''
    - Obtiene los mejores promedios de puntos por partido.
    - Recibe un lista de jugadores y el jugador con menos puntos por partido.
    - Retorna None si la lista esta vacia sino retorna una lista
      sin el jugador con menos puntos por partido.
    '''
    retorno = None
    lista_mejores_promedios = []
    
    if lista_jugadores != []:
        for jugador in lista_jugadores:
            if jugador["nombre"] != jugador_menos_puntos["nombre"]:
                lista_mejores_promedios.append(jugador)
                retorno = lista_mejores_promedios
    return retorno
  
def obtener_jugador_mayores_logros (lista_jugadores:list)->dict:
    '''
    - Obtiene el jugador con los mayores logros.
    - Recibe una lista de jugadores.
    - Retorna None si la lista esta vacia sino retorna un jugador.
    '''
    retorno = None
    mayores_cantidad_logros = 0
    
    if lista_jugadores != []:
        for jugador in lista_jugadores:
            if len(jugador["logros"]) > mayores_cantidad_logros:
                mayores_cantidad_logros = len(jugador["logros"])
                retorno = jugador
            
    return retorno
        
def obtener_jugadores_mayores_temporadas (lista_jugadores:list)->list:
    '''
    - Obtiene los jugadores con el mayor cantidad de temporadas.
    - Recibe una lista y un dato a evaluar.
    - Retorna None si la lista esta vacia sino retorna una lista de jugadores.
    '''
    retorno = None
    mayor_dato = 0
    nueva_lista = []
        
    if lista_jugadores != []:
        for jugador in lista_jugadores:
            for valor in jugador["estadisticas"]:
                if valor == "temporadas" and jugador["estadisticas"]["temporadas"] > mayor_dato:
                        mayor_dato = jugador["estadisticas"]["temporadas"]
                        mayor_jugador = jugador
        
        nueva_lista.append(mayor_jugador)
        for jugador in lista_jugadores:
            if jugador["nombre"] != nueva_lista[0]["nombre"]:
                for valor in jugador["estadisticas"]:
                    if valor == "temporadas" and jugador["estadisticas"]["temporadas"] == nueva_lista[0]["estadisticas"]["temporadas"]:
                        mayor_jugador = jugador
        nueva_lista.append (mayor_jugador)
        return nueva_lista
    

#=====================================================================

#23 Bonus
