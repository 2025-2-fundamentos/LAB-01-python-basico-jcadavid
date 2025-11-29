"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    data = {}
    with open("files/input/data.csv", newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            letter = row[0]
            val = int(row[1])
            if letter not in data:
                data[letter] = []
            data[letter].append(val)
            
    result = []
    for letter in sorted(data.keys()):
        vals = data[letter]
        result.append((letter, max(vals), min(vals)))
        
    return result
