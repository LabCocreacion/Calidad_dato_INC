# Leer el excel, limpiar campos irrelevantes y generar pares
import pandas as pd
import json
from pathlib import Path

input_file = Path("data/raw/descarga_calidad_datos_purgada.xlsx")
output_file = Path("data/processed/dataset.json")

df = pd.read_excel(input_file)

records = []
for _, row in df.iterrows():
    record = {
        "text": str(row["Enfermedad"]) + " " + str(row["Motivo Atención"]) + " " + str(row["Observación"]),
        "T": row["T"],
        "N": row["N"],
        "M": row["M"],
        "Estadio": row["Est"]
    }
    records.append(record)

with open(output_file, "w", encoding="utf8") as f:
    for r in records:
        try:
            text = r["text"].replace("\n", " ").replace("\r", " ")
            r["text"] = text
            json.dump(r, f, ensure_ascii=False)
            f.write("\n")
        except Exception as e:
            print("Error al procesar:", r)
            print(e)