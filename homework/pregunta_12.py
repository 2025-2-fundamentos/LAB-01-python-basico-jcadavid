"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    sums = {}
    with open("files/input/data.csv", newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            letter = row[0]
            encoded_dict = row[4]
            pairs = encoded_dict.split(',')
            row_sum = 0
            for pair in pairs:
                _, v = pair.split(':')
                row_sum += int(v)
            
            sums[letter] = sums.get(letter, 0) + row_sum
            
    return dict(sorted(sums.items()))
