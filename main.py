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

lista_jugadores = leer_archivo_json("pp_lab1_gimenez_hugo\dt.json")


def mostrar_nombre_y_dato(lista:list, constante, dato:str)->bool:
    '''
    - Muestra el nombre y el dato pasado por parametro.
    - Recibe una lista, una constante para formatear el print y
      y el dato.
    - No retorna nada.
    '''
    for jugador in lista:
        print("Nombre: {0} - {1}: {2}".format(jugador["nombre"], constante, jugador[dato]))
        
#mostrar_nombre_y_dato(lista_jugadores, "Posicion" "posicion")

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

def mostrar_un_jugador_nombre_dato (lista:list, indice:str, dato:str)->bool:
    '''
    - Muestra el nombre de un jugador.
    - Recibe una lista y el indice de la lista.
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
        for clave in jugador["estadisticas"].keys():
            print("{0} - {1}".format(clave, jugador["estadisticas"][clave]).capitalize(),end="\n")
        
        retorno = jugador
        
    return retorno

# mostrar_un_jugador_nombre_dato(lista_jugadores, "10", "posicion")
# jugador = mostrar_estadisticas_jugador (lista_jugadores, "10")

def formatear_nombre_a_guardar(jugador:dict)->str:
    '''
    - Da formato al string tomando el nombre del jugador para guardar en un csv.
    - Recibe un jugador por parametro.
    - Retorna un string para el nombre del csv.
    '''
    nombre = jugador["nombre"].replace(" ", "_")
    print(nombre)
    nombre_a_guardar = "pp_lab1_gimenez_hugo/estadistica_{}".format(nombre)
    return nombre_a_guardar

#nombre_csv = formatear_nombre_a_guardar(jugador)

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

#dato_a_guardar = parser_csv(jugador)
        
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

#guardar_archivo(nombre_csv, dato_a_guardar)

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

# logros  = obtener_logros_jugador(lista_jugadores, "larry")
# mostrar_logros_jugador(logros)

def sumar_dato_jugador (lista:list, dato:str)->float:
    '''
    - 
    - Si la lista esta vacia retorna -1.
    '''
    retorno = -1
    suma = 0
    
    if lista != []:
        for jugador in lista:
            for valor in jugador["estadisticas"]:
                if valor == dato:
                    puntos = jugador["estadisticas"][valor]
                    suma += puntos
                    retorno = suma            
    return retorno

# total_puntos = sumar_dato_jugador(lista_jugadores, "promedio_puntos_por_partido")
# print(total_puntos)

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
 
#05
def obtener_promedio_puntos_partidos_del_equipo (lista:list, dato:str)->float:
    ''' 
    - Calcula el promedio del dato recibido en la lista.
    - Recibe como parametros una lista y el dato a calcular.
    - Retorna el promedio calculado.
    - Si la lista esta vacia retorna -1.
    '''
    retorno = -1

    if lista != []:
        suma = sumar_dato_jugador(lista, dato)
        cantidad = len(lista)
        promedio = dividir(suma, cantidad)
        retorno = promedio
    
    return retorno

#print(obtener_promedio_puntos_partidos_del_equipo (lista_jugadores, "promedio_puntos_por_partido"))

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

#print(es_miembro_salon_de_la_fama (lista_jugadores, "michael"))
#07 rebotes totales
def obtener_jugador_mayor_dato (lista_jugadores:list, dato:str)->dict:
    '''
    -
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

# jugador = obtener_jugador_mayor_dato(lista_jugadores, "rebotes_totales")
# print(jugador)
# print("Nombre: {0} - Rebotes Totales: {1}".format(jugador["nombre"], jugador["estadisticas"]["rebotes_totales"]))

#08 tiros de campo
def obtener_jugador_mayor_dato (lista_jugadores:list, dato:str)->dict:
    '''
    -
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

# jugador = obtener_jugador_mayor_dato(lista_jugadores, "porcentaje_tiros_de_campo")
# print(jugador)
# print("Nombre: {0} - Tiros de Campo: {1}".format(jugador["nombre"], jugador["estadisticas"]["porcentaje_tiros_de_campo"]))

#09 asistencia totoles
def obtener_jugador_mayor_dato (lista_jugadores:list, dato:str)->dict:
    '''
    -
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

# jugador = obtener_jugador_mayor_dato(lista_jugadores, "asistencias_totales")
# print("Nombre: {0} - Asistencias Totales: {1}".format(jugador["nombre"], jugador["estadisticas"]["asistencias_totales"]))

#10 Permitir al usuario ingresar un valor y mostrar los jugadores 
# que han promediado más puntos por partido que ese valor
def obtener_mayores (lista_jugadores:list, numero:str)->list:
    '''
    -
    '''
    retorno = None
    nueva_lista = []
    numero = float(numero)
    
    if lista_jugadores != []:
        for jugador in lista_jugadores:
            for valor in jugador["estadisticas"]:
                if valor == "promedio_puntos_por_partido" and jugador["estadisticas"][valor] > numero:
                    nueva_lista.append(jugador)
                    retorno = nueva_lista
                    #print(retorno)
    return retorno
            
def mostrar_nombre_y_dato_jugadores (lista:list, constante, dato:str)->bool:
    '''
    - Muestra el nombre y el dato pasado por parametro.
    - Recibe una lista, una constante para formatear el print y
      y el dato.
    - No retorna nada.
    '''
    for jugador in lista:
        #print(jugador)
        print("Nombre: {0} - {1}: {2}".format(jugador["nombre"], constante, jugador["estadisticas"][dato]))
        
# lista_mayores = (obtener_mayores (lista_jugadores, "20"))
# mostrar_nombre_y_dato_jugadores (lista_mayores, "Promedio puntos por Partido", "promedio_puntos_por_partido")

#11 Permitir al usuario ingresar un valor y mostrar los jugadores 
# que han promediado más rebotes por partido que ese valor
def obtener_mayores (lista_jugadores:list, numero:str)->list:
    '''
    -
    '''
    retorno = None
    nueva_lista = []
    numero = float(numero)
    
    if lista_jugadores != []:
        for jugador in lista_jugadores:
            for valor in jugador["estadisticas"]:
                if valor == "promedio_rebotes_por_partido" and jugador["estadisticas"][valor] > numero:
                    nueva_lista.append(jugador)
                    retorno = nueva_lista
                    #print(retorno)
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
        
# lista_mayores = (obtener_mayores (lista_jugadores, "5")) #12 rompe -- validar
# mostrar_nombre_y_dato_jugadores (lista_mayores, "Promedio rebotes por Partido", "promedio_rebotes_por_partido")

#12) Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado
#más asistencias por partido que ese valor
def obtener_mayores (lista_jugadores:list, numero:str)->list:
    '''
    -
    '''
    retorno = None
    nueva_lista = []
    numero = float(numero)
    
    if lista_jugadores != []:
        for jugador in lista_jugadores:
            for valor in jugador["estadisticas"]:
                if valor == "promedio_asistencias_por_partido" and jugador["estadisticas"][valor] > numero:
                    nueva_lista.append(jugador)
                    retorno = nueva_lista
                    #print(retorno)
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
        
# lista_mayores = (obtener_mayores (lista_jugadores, "9")) #12 rompe -- validar
# mostrar_nombre_y_dato_jugadores (lista_mayores, "Promedio asistencias por Partido", "promedio_asistencias_por_partido")

#13 Calcular y mostrar el jugador con la mayor cantidad de robos totales.
def obtener_jugador_mayor_dato (lista_jugadores:list, dato:str)->dict:
    '''
    -
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

# jugador = obtener_jugador_mayor_dato(lista_jugadores, "robos_totales")
# print("Nombre: {0} - Robos totales: {1}".format(jugador["nombre"], jugador["estadisticas"]["robos_totales"]))

#14 Calcular y mostrar el jugador con la mayor cantidad de bloqueos totales
def obtener_jugador_mayor_dato (lista_jugadores:list, dato:str)->dict:
    '''
    -
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

# jugador = obtener_jugador_mayor_dato(lista_jugadores, "bloqueos_totales")
# print("Nombre: {0} - Bloqueos totales: {1}".format(jugador["nombre"], jugador["estadisticas"]["bloqueos_totales"]))

#15 Permitir al usuario ingresar un valor y mostrar los jugadores 
# que hayan tenido un porcentaje de tiros libres superior a ese valor.

def obtener_mayores (lista_jugadores:list, numero:str)->list:
    '''
    -
    '''
    retorno = None
    nueva_lista = []
    numero = float(numero)
    
    if lista_jugadores != []:
        for jugador in lista_jugadores:
            for valor in jugador["estadisticas"]:
                if valor == "porcentaje_tiros_libres" and jugador["estadisticas"][valor] > numero:
                    nueva_lista.append(jugador)
                    retorno = nueva_lista
                    #print(retorno)
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
        
# lista_mayores = (obtener_mayores (lista_jugadores, "86")) #89 rompe -- validar
# mostrar_nombre_y_dato_jugadores (lista_mayores, "Porcentaje de tiros libres", "porcentaje_tiros_libres")

#Calcular y mostrar el promedio de puntos por partido del equipo 
# excluyendo al jugador con la menor cantidad de puntos por partido

def jugador_menores_puntos_por_partido (lista_jugadores:list)->dict:
    '''
    -
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
                    #print(menor_dato)
                    retorno = jugador
    return retorno

#jugador_menos_puntos = jugador_menores_puntos_por_partido(lista_jugadores)
#print(jugador_menos_puntos)

def obtener_mejores_promedios (lista_jugadores:list, jugador_menos_puntos:dict)->list:
    '''
    -
    '''
    retorno = None
    lista_mejores_promedios = []
    
    if lista_jugadores != []:
        for jugador in lista_jugadores:
            if jugador["nombre"] != jugador_menos_puntos["nombre"]:
                lista_mejores_promedios.append(jugador)
                retorno = lista_mejores_promedios
    return retorno
           
#lista_mejores_promedios = obtener_mejores_promedios(lista_jugadores, jugador_menos_puntos)

def obtener_promedio_puntos_partidos_del_equipo (lista:list, dato:str)->float:
    ''' 
    - Calcula el promedio del dato recibido en la lista.
    - Recibe como parametros una lista y el dato a calcular.
    - Retorna el promedio calculado.
    - Si la lista esta vacia retorna -1.
    '''
    retorno = -1

    if lista != []:
        suma = sumar_dato_jugador(lista, dato)
        cantidad = len(lista)
        promedio = dividir(suma, cantidad)
        retorno = promedio
    
    return retorno

#print(obtener_promedio_puntos_partidos_del_equipo (lista_mejores_promedios, "promedio_puntos_por_partido"))

#17 Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos









#===================================================================================

def ordenar_por_key (lista_jugadores:list, dato:str, orden:bool=True)->list:
    '''
    - Ordena la lista segun el dato/key de forma ascendente o descendente.
    - Recibe una lista por parametro, el dato a ordenar y el tipo de orden.
    - True = Ascendente o False = Descendente.
    - Retorna la lista ordenada.
    - Si la lista esta vacia retorna -1.
    '''
    retorno = -1
    
    if lista_jugadores != []:
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

#print(ordenar_por_key(lista_jugadores, ""))