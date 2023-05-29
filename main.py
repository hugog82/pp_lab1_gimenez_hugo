from funciones import leer_archivo_json
from menu import dream_team_app

lista_jugadores = leer_archivo_json("./pp_lab1_gimenez_hugo/dt.json")

dream_team_app (lista_jugadores)
