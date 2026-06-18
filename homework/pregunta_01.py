"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
import pandas as pd
import re

def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    file_path = "files/input/clusters_report.txt"
    with open(file_path, "r") as file:
        lines = file.readlines()

    columns = [re.split(r"\s{2,}", line.strip()) for line in lines[:2]]

    columns = [
        col1 + " " + columns[1].pop(0) if re.search(r"\bde\b", col1) else col1
        for col1 in columns[0]
    ]

    columns = [col.lower().replace(" ", "_") for col in columns]

    data = "".join(lines[4:])
    data = re.split(r"\n\s*\n", data)
    data = data[:-1]

    rows = []

    for row in data:
          row = re.split(r"\s{2,}", row.strip(), maxsplit=3)
          row[0] = int(row[0])
          row[1] = int(row[1])
          row[2] = float(row[2].replace("%", "").replace(",", "."))
          row[3] = re.sub(r"\s+", " ", row[3].replace("\n", " ").replace(".", "")).strip()
          rows.append(row)

    df = pd.DataFrame(rows, columns=columns)

    return df
