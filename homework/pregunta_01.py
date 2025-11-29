"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """

    total = 0
    with open("files/input/data.csv", newline='', encoding='utf-8') as csv_data:
        reader = csv.reader(csv_data, delimiter='\t')
        for row in reader:
            try:
                total += int(row[1])
            except (ValueError, IndexError):
                pass
    return total

if __name__ == '__main__':
    print(pregunta_01())



