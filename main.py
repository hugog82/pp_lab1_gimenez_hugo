import funciones
import menu

lista_jugadores = funciones.leer_archivo_json("pp_lab1_gimenez_hugo\dt.json")

menu.dream_team_app (lista_jugadores)
