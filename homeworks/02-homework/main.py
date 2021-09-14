import csv

file = open("../../data/atp_matches_2012.csv")

data = csv.reader(file)

"""# Integrantes del equipo:

Contesta las siguientes preguntas, __sin__ utilizar la librería Pandas.

- Felipe López Valdez

# Manejo de datos
- Extrae las categorías del archivo.
"""

# categorías
categories = next(data)


"""- Crea una lista con cada partido, donde los datos de cada partido sean un diccionario. Con las categorías como llave y el valor como el contenido.

"""

matches = []
for d in data:
    match_dic = dict()
    for k, v in zip(categories, d):
        match_dic[k] = v
    matches.append(match_dic)


"""# Filtrado de datos
- Haz un conjunto de todos los nombres de ganadores de partidos.

"""

# ganadores
winners_names = []
for match in matches:
    winner_name = match["loser_name"]
    if winner_name not in winners_names:
        winners_names.append(winner_name)

"""- Haz un conjunto de todos los nombres de perdedores de partidos.

"""

# perdedores
losers_names = []
for match in matches:
    loser_name = match["loser_name"]
    if loser_name not in losers_names:
        losers_names.append(loser_name)

"""- Enlista qué jugadores no han perdido ningún partido. """

# no han perdido
no_losers_names = []
for winner in winners_names:
    if winner not in losers_names:
        if winner not in no_losers_names:
            no_losers_names.append(winner)

"""- ¿Cuántos jugadores no han perdido ningún partido?

"""

# número de jugadores que no han perdido
num_no_losers = len(no_losers_names)

"""- Enlista qué jugadores no han ganado ningún partido."""

# no han ganado
no_winners_names = []
for loser in no_losers_names:
    if loser not in winners_names:
        if loser not in no_winners_names:
            no_winners_names.append(loser)

"""- ¿Cuántos jugadores no han ganado ningún partido?"""

# número de jugadores que no han ganado
num_no_winners = len(no_winners_names)

"""- Haz una lista diciendo cuántos partidos ha ganado cada jugador."""

# cantidad de partidos ganados por jugador
win_matches_per_player = {}
for match in matches:
    winner_name = match["winner_name"]
    try:
        win_matches_per_player[winner_name] += 1
    except:
        win_matches_per_player[winner_name] = 1

"""- Haz una lista diciendo cuántos partidos ha perdido cada jugador"""

# cantidad de partidos perdidos por jugador
lose_matches_per_player = {}
for match in matches:
    loser_name = match["loser_name"]
    try:
        lose_matches_per_player[loser_name] += 1
    except:
        lose_matches_per_player[loser_name] = 1

"""- Obtén el jugador con más partidos ganados."""

# jugador con más partidos ganados
name_mvp = ""
win_matches_mvp = 0
for player in win_matches_per_player:
    player_win_matches = win_matches_per_player[player]
    if player_win_matches > win_matches_mvp:
        name_mvp = player
        win_matches_mvp = player_win_matches

"""- Obtén el jugador con más partidos perdidos"""

# jugador con más partidos perdidos
name_mlp = ""
lose_matches_mlp = 0
for player in lose_matches_per_player:
    player_lose_matches = lose_matches_per_player[player]
    if player_lose_matches > lose_matches_mlp:
        name_mlp = player
        lose_matches_mlp = player_lose_matches

"""- Obtén todos los jugadores que hayan llegado a semifinales"""

# Semifinalistas
semifinalists = []
for match in matches:
    match_round = match["round"]
    if match_round == "SF":
        winner_name = match["winner_name"]
        loser_name = match["loser_name"]
        if winner_name not in semifinalists:
            semifinalists.append(winner_name)
        if loser_name not in semifinalists:
            semifinalists.append(loser_name)

"""- Obtén todos los jugadores que hayan ganado una final."""

# Campeones
champions = []
for match in matches:
    match_round = match["round"]
    if match_round == 'F':
        name = match["winner_name"]
        if name not in champions:
            champions.append(name)

"""-

# Ordenamiento
- Obtén los 10 jugadores con más partidos ganados y especifica cuántos partidos ganaron.
"""

# top 10
list_winners_matches = []
for player in win_matches_per_player:
    list_winners_matches.append((player, win_matches_per_player[player]))
list_winners_matches.sort(key=lambda x: x[1], reverse=True)
top_10_winners = list_winners_matches[:10]

"""- Obtén los 10 jugadores con más partidos perdidos y especifica cuántos partidos perdieron."""

# top 10
list_losers_matches = []
for player in lose_matches_per_player:
    list_losers_matches.append((player, lose_matches_per_player[player]))
list_losers_matches.sort(key=lambda x: x[1], reverse=True)
top_10_losers = list_losers_matches[:10]

"""- Obtén una lista con los tipos de canchas que existen (pasto, arcilla, etc)"""

# Tipos de canchas
courts = []
for match in matches:
    surface = match["surface"]
    if surface not in courts:
        courts.append(surface)

"""- Para cada tipo de cancha: Obtén una lista con los tres jugadores con más finales ganadas, y la cantidad de finales ganadas."""
players_per_surface = {}
for match in matches:
    winner_name = match["winner_name"]
    surface = match["surface"]
    match_round = match["round"]
    if match_round == 'F':
        try:
            players_per_surface[surface][winner_name] += 1
        except:
            try:
                players_per_surface[surface][winner_name] = 1
            except:
                players_per_surface[surface] = {}

top3_per_court = {}
for surface in players_per_surface:
    players = []
    for player in players_per_surface[surface]:
        players.append((player, players_per_surface[surface][player]))
    players.sort(key=lambda x: x[1], reverse=True)
    top3_per_court[surface] = players[:3]

"""# Pregunta ¿Quién fue el mejor jugador de la ATP de 2012 a 2017?"""
