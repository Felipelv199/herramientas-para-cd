import csv

file = open("../../data/atp_matches_2012.csv")

data = csv.reader(file)

# Categorias
categories = next(data)

# Partidos
matches = []
for d in data:
    match_dic = dict()
    for k, v in zip(categories, d):
        match_dic[k] = v
    matches.append(match_dic)

# Ganadores
winners = [match["winner_name"] for match in matches]

# Perdedores
losers = [match["loser_name"] for match in matches]

# No han perdido
no_losers = []
for winner in winners:
    if winner not in losers:
        if winner not in no_losers:
            no_losers.append(winner)
print(no_losers)
