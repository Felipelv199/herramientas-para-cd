import csv
from dataclasses import dataclass
""" file = open("../data/marathon_results_2015.csv")

lines = file.readlines()

categories = lines[0].split(',')

print(categories)

participantes = []
for line in lines[1:]:
    participantes.append(line.split())
print(participantes[0]) """

""" 
# Abrir y leer archivos usando csv

import csv

file = open("../data/marathon_results_2015.csv")
data = csv.reader(file)
categories = next(data)
participante = next(data)
print(f"{categories[2]:20} {categories[3]:5} {categories[7]:10}")
print(f"{participante[2]:20} {participante[3]:5} {participante[7]:10}") 
"""
""" 
# Guardado de datos en un diccionario
file = open("../data/marathon_results_2015.csv")
data = csv.reader(file)
categories = next(data)
participante = next(data)

corredor = dict()
for c, p in zip(categories, participante):
    corredor[c] = p
print(corredor)
"""
""" # Formateo para todos los participantes
file = open("../data/marathon_results_2015.csv")
data = csv.reader(file)
categories = next(data)
corredores = []
for participante in data:
    corredor = dict()
    for c, p in zip(categories, participante):
        corredor[c] = p
    corredores.append(corredor)
print(corredores[0])
"""
""" # Guardado de datos como objeto


@dataclass
class Corredor:
    nombre: str = ""
    pais: str = ""
    edad: int = 0
    tiempo: str = ""


file = open("../data/marathon_results_2015.csv")
data = csv.reader(file)
categories = next(data)
corredores_dic = []
for participante in data:
    corredor_dic = dict()
    for c, p in zip(categories, participante):
        corredor_dic[c] = p
    corredores_dic.append(corredor_dic)

corredores_list = []

for corredor_dic in corredores_dic:
    corredor_obj = Corredor()
    corredor_obj.nombre = corredor_dic["Name"]
    corredor_obj.edad = corredor_dic["Age"]
    corredor_obj.tiempo = corredor_dic["Official Time"]
    corredor_obj.pais = corredor_dic["Country"]
    corredores_list.append(corredor_obj)

ganador = corredores_list[0]
print(ganador)
"""


@dataclass
class Corredor:
    nombre: str = ""
    pais: str = ""
    edad: int = 0
    tiempo: str = ""


# Filtrado de datos
# Generación de listas
file = open("../data/marathon_results_2015.csv")
data = csv.reader(file)

categorias = next(data)

varones = [Corredor(nombre=p[2], pais=p[7], tiempo=p[21])
           for p in data if p[4] == "F"]
print(varones)
