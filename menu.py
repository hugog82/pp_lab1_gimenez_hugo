import funciones
    
def imprimir_menu_dream_team ():
    '''
    - Imprime por pantalla el menu creado.
    - Utiliza la funcion imprimir_dato ().
    - No retorna nada.
    '''
    funciones.imprimir_dato("Menú de opciones:")
    funciones.imprimir_dato("1. Mostrar la lista de todos los jugadores \
del Dream Team.")
    funciones.imprimir_dato("2. Mostrar estadisticas de un jugador.")            
    funciones.imprimir_dato("3. Guardar estadisticas.")
    funciones.imprimir_dato("4. Mostrar logros de un jugador.")
    funciones.imprimir_dato("5. Mostrar el promedio de puntos por \
partido del Dream Team y sus nombre ordenados de forma ascendente.")
    funciones.imprimir_dato("6. Mostrar si un jugador es miembro del \
salon de la fama.")    
    funciones.imprimir_dato("7. Mostrar el jugador con la mayor \
cantidad de rebotes totales.")
    funciones.imprimir_dato("8. Mostrar el jugador con el mayor \
porcentaje de tiros de campo.")    
    funciones.imprimir_dato("9. Mostrar el jugador con la mayor \
cantidad de asistencias totales.")
    funciones.imprimir_dato("10. Mostrar los jugadores que han \
promediado más puntos por partido segun el valor ingresado.")                
    funciones.imprimir_dato("11. Mostrar los jugadores que han \
promediado más rebotes por partido segun el valor ingresado.")
    funciones.imprimir_dato("12. Mostrar los jugadores que han \
promediado más asistencias por partido segun el valor ingresado.")    
    funciones.imprimir_dato("13. Mostrar el jugador con la mayor \
cantidad de robos totales.")
    funciones.imprimir_dato("14. Mostrar el jugador con la mayor \
cantidad de bloqueos totales.")    
    funciones.imprimir_dato("15. Mostrar los jugadores que hayan \
tenido un porcentaje de tiros libres superior a un valor ingresado.")
    funciones.imprimir_dato("16. Mostrar el promedio de puntos por \
partido del Dream Team excluyendo el jugador con menos puntos.")
    funciones.imprimir_dato("17. Mostrar el jugador con la mayor \
cantidad de logros obtenidos.")    
    funciones.imprimir_dato("18. Mostrar los jugadores que hayan \
tenido un porcentaje de tiros triples superior a un valor ingresado.")
    funciones.imprimir_dato("19. Mostrar el jugador con la mayor \
cantidad de temporadas jugadas.")    
    funciones.imprimir_dato("20. Mostrar los jugadores ordenados por \
posicion en la cancha, que hayan tenido un porcentaje de tiros \n    \
de campo superior a un valor ingresado.")
    funciones.imprimir_dato("23. Mostrar y guardar la posicion de cada \
jugador en cada uno de los siguientes rankings. Puntos - \n    Rebotes - \
Asistencias - Robos.")                         
    funciones.imprimir_dato("0. Salir.")
       
def menu_principal_dream_team (): 
    '''
     - Muestra el menu principal con las opciones.
     - Se le pedira al usuario que ingrese una opcion del menu.
     - Se validara que la opcion ingresada sea correcta usando
       la funcion es_entero ().
     - Si la opcion ingresada es correcta retorna dicha opcion.
     - Si la opcion ingresada es incorrecta retorna None.
     - 
    '''
    imprimir_menu_dream_team ()
    
    opcion = input("\nIngrese la opción deseada: ")
    
    retorno = funciones.es_entero (opcion)
    
    return retorno

def dream_team_app (lista:list):
    '''
    - Se encarga de la ejecucion principal de nuestro programa.
    - Recibe por parametro la lista de jugador.
    - Retorna False si la lista esta vacia sino retorna True.
    '''
    retorno = False
    
    if lista != []:    
        while True:
            opcion = menu_principal_dream_team ()
            match opcion:
                case "1":
                        funciones.mostrar_nombres_y_datos(lista, "Posicion", "posicion")
                case "2":
                        funciones.mostrar_indice_y_nombre(lista)
                        while True:
                            indice = input("\nIngrese el indice ó 'v' para volver al menu anterior: ")
                            if funciones.es_entero(indice) != None:
                                indice = int(indice)
                                if indice >= 0 and indice < 12:
                                    indice = str(indice)
                                    jugador_a_guardar = funciones.mostrar_estadisticas_jugador(lista, indice)
                                else:
                                    print("ERROR! La opcion ingresada es incorrecta.\n")
                                    funciones.mostrar_indice_y_nombre(lista) 
                            elif funciones.es_letra(indice) == "v" or funciones.es_letra(indice) == "V":
                                break
                            else:
                                print("ERROR! La opcion ingresada es incorrecta.\n")
                                funciones.mostrar_indice_y_nombre(lista)
                case "3":
                        nombre_csv = funciones.formatear_nombre_a_guardar(jugador_a_guardar)
                        dato_a_guardar = funciones.parser_csv(jugador_a_guardar)
                        funciones.guardar_archivo(nombre_csv, dato_a_guardar)
                case "4":#falta validar mejor
                        funciones.mostrar_nombres_y_datos(lista, "Posicion", "posicion")
                        while True:
                            nombre = input("\nIngrese el nombre del jugador ó 'salir' para volver al menu anterior.\n")
                            if funciones.obtener_logros_jugador(lista, nombre) != None:
                                jugador = funciones.obtener_logros_jugador(lista, nombre)
                                funciones.mostrar_logros_jugador(jugador)
                                print(input("Presione enter para continuar..."))
                                funciones.mostrar_nombres_y_datos(lista, "Posicion", "posicion")                             
                            else:
                                print("No se encontro al jugador...")
                                break
                case "5":
                        promedio = funciones.obtener_promedio_puntos_partidos_del_equipo (lista, "promedio_puntos_por_partido")
                        print("Promedio de puntos por partido del equipo: {:.2f}\nJugadores:".format(promedio))
                        lista_ordenada = funciones.ordenar_por_key(lista, "nombre")
                        funciones.mostrar_nombres_y_datos(lista_ordenada, "Posicion", "posicion")
                case "6": #falta validar mejor
                        funciones.mostrar_nombres_y_datos(lista, "Posicion", "posicion")
                        while True:
                            nombre = input("\nIngrese el nombre del jugador: ó 'salir' para volver al menu anterior.\n")
                            if funciones.es_solo_texto(nombre):
                                if funciones.es_miembro_salon_de_la_fama (lista, nombre):
                                    print("Es miembro del salon de la fama.\n")                             
                                else:
                                    print("No es miembro.")
                                    break
                            else:
                                print("ERROR! La opcion ingresada es incorrecta.\n")
                case "7":
                        jugador = funciones.obtener_jugador_mayor_dato(lista, "rebotes_totales")
                        funciones.mostrar_jugador_nombre_dato (jugador, "Rebotes totales", "rebotes_totales")                          
                case "8":
                        jugador = funciones.obtener_jugador_mayor_dato(lista, "porcentaje_tiros_de_campo")
                        funciones.mostrar_jugador_nombre_dato(jugador, "Porcentaje tiros de campo", "porcentaje_tiros_de_campo")
                case "9":
                        jugador = funciones.obtener_jugador_mayor_dato(lista, "asistencias_totales")
                        funciones.mostrar_jugador_nombre_dato(jugador, "Asistencias totales", "asistencias_totales")      
                case "10":
                        while True:
                            valor_ingresado = input("\nIngrese un valor (debe ser menor/igual a '30') ó '0' para salir.\n")
                            if funciones.es_entero(valor_ingresado) != None and funciones.es_entero(valor_ingresado) != "0":
                                valor_ingresado = int(valor_ingresado)
                                if valor_ingresado > 0 and valor_ingresado <= 30:
                                    valor_ingresado = str(valor_ingresado)
                                    lista_mayores = (funciones.obtener_mayores (lista, "promedio_puntos_por_partido", valor_ingresado))
                                    funciones.mostrar_nombre_y_dato_jugadores (lista_mayores, "Promedio puntos por Partido", "promedio_puntos_por_partido")
                            elif funciones.es_entero(valor_ingresado) == "0":
                                break
                            else:
                                print("ERROR! La opcion ingresada es incorrecta.\n")                                                                  
                case "11":
                        while True:
                            valor_ingresado = input("\nIngrese un valor (debe ser menor/igual a '11') ó '0' para salir.\n")
                            if funciones.es_entero(valor_ingresado) != None and funciones.es_entero(valor_ingresado) != "0":
                                valor_ingresado = int(valor_ingresado)
                                if valor_ingresado > 0 and valor_ingresado <= 11:
                                    valor_ingresado = str(valor_ingresado)
                                    lista_mayores = (funciones.obtener_mayores (lista, "promedio_rebotes_por_partido", valor_ingresado))
                                    funciones.mostrar_nombre_y_dato_jugadores (lista_mayores, "Promedio rebotes por Partido", "promedio_rebotes_por_partido")
                            elif funciones.es_entero(valor_ingresado) == "0":
                                break
                            else:
                                print("ERROR! La opcion ingresada es incorrecta.\n")                                    
                case "12":
                        while True:
                            valor_ingresado = input("\nIngrese un valor (debe ser menor/igual a '11') ó '0' para salir.\n")
                            if funciones.es_entero(valor_ingresado) != None and funciones.es_entero(valor_ingresado) != "0":
                                valor_ingresado = int(valor_ingresado)
                                if valor_ingresado > 0 and valor_ingresado <= 11:
                                    valor_ingresado = str(valor_ingresado)
                                    lista_mayores = (funciones.obtener_mayores (lista, "promedio_asistencias_por_partido", valor_ingresado))
                                    funciones.mostrar_nombre_y_dato_jugadores (lista_mayores, "Promedio asistencias por Partido", "promedio_asistencias_por_partido")
                            elif funciones.es_entero(valor_ingresado) == "0":
                                break
                            else:
                                print("ERROR! La opcion ingresada es incorrecta.\n")                                                       
                case "13":
                        jugador = funciones.obtener_jugador_mayor_dato(lista, "robos_totales")
                        funciones.mostrar_jugador_nombre_dato(jugador, "Robos totales", "robos_totales")                                   
                case "14":
                        jugador = funciones.obtener_jugador_mayor_dato(lista, "bloqueos_totales")
                        funciones.mostrar_jugador_nombre_dato(jugador, "Bloqueos totales", "bloqueos_totales")                               
                case "15":
                        while True:
                            valor_ingresado = input("\nIngrese un valor (debe ser menor/igual a '88') ó '0' para salir.\n")
                            if funciones.es_entero(valor_ingresado) != None and funciones.es_entero(valor_ingresado) != "0":
                                valor_ingresado = int(valor_ingresado)
                                if valor_ingresado > 0 and valor_ingresado <= 88:
                                    valor_ingresado = str(valor_ingresado)
                                    lista_mayores = (funciones.obtener_mayores (lista, "porcentaje_tiros_libres", valor_ingresado)) #89 rompe -- validar!
                                    funciones.mostrar_nombre_y_dato_jugadores (lista_mayores, "Porcentaje de tiros libres", "porcentaje_tiros_libres")
                            elif funciones.es_entero(valor_ingresado) == "0":
                                break
                            else:
                                print("ERROR! La opcion ingresada es incorrecta.\n")
                case "16":
                        jugador_menos_puntos = funciones.jugador_menores_puntos_por_partido(lista)
                        lista_mejores_promedios = funciones.obtener_mejores_promedios(lista, jugador_menos_puntos)
                        promedio = funciones.obtener_promedio_puntos_partidos_del_equipo (lista_mejores_promedios, "promedio_puntos_por_partido")
                        print("Promedio de puntos por partido del equipo: {:.2f}".format(promedio))                                                                       
                case "17":
                        jugador_con_mas_logros = funciones.obtener_jugador_mayores_logros (lista)
                        print("Jugador con la mayor cantidad de logros:\nNombre: {0} - Logros: {1}".format(jugador_con_mas_logros["nombre"], len(jugador_con_mas_logros["logros"])))                                                                                                                            
                case "18":
                        while True:
                            valor_ingresado = input("\nIngrese un valor (debe ser menor/igual a '48') ó '0' para salir.\n")
                            if funciones.es_entero(valor_ingresado) != None and funciones.es_entero(valor_ingresado) != "0":
                                valor_ingresado = int(valor_ingresado)
                                if valor_ingresado > 0 and valor_ingresado <= 48:
                                    valor_ingresado = str(valor_ingresado)
                                    lista_mayores = (funciones.obtener_mayores (lista, "porcentaje_tiros_triples", valor_ingresado)) #49 rompe -- validar
                                    funciones.mostrar_nombre_y_dato_jugadores (lista_mayores, "Porcentaje de tiros triples", "porcentaje_tiros_triples")
                            elif funciones.es_entero(valor_ingresado) == "0":
                                break
                            else:
                                print("ERROR! La opcion ingresada es incorrecta.\n")                                  
                case "19":
                        jugador = funciones.obtener_jugador_mayor_dato(lista, "temporadas")            
                        funciones.mostrar_jugador_nombre_dato(jugador, "Temporadas", "temporadas")                                    
                case "20":
                        while True:
                            valor_ingresado = input("\nIngrese un valor (debe ser menor/igual a '53') ó '0' para salir.\n")
                            if funciones.es_entero(valor_ingresado) != None and funciones.es_entero(valor_ingresado) != "0":
                                valor_ingresado = int(valor_ingresado)
                                if valor_ingresado > 0 and valor_ingresado <= 53:
                                    valor_ingresado = str(valor_ingresado)
                                    lista_mayores = (funciones.obtener_mayores (lista, "porcentaje_tiros_triples", valor_ingresado)) #54 rompe -- validar
                                    funciones.mostrar_nombre_y_dato_jugadores (lista_mayores, "Porcentaje de tiros de campo", "porcentaje_tiros_de_campo")
                            elif funciones.es_entero(valor_ingresado) == "0":
                                break
                            else:
                                print("ERROR! La opcion ingresada es incorrecta.\n")
                case "23":
                        pass                                        
                case "0":
                        break   
                case _:
                        print("La opcion ingresada no es válida! Ingrese una opcion del Menu...\n")
            print(input("Presione enter para continuar..."))
        retorno = True
    return retorno