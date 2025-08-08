#Evaluación automática de los datos estructurados
import spacy
from spacy.pipeline import EntityRuler
import json

#Cargamos spaCy con reglas
nlp = spacy.blank("es")
ruler = nlp.add_pipe("entity_ruler")
ruler.from_disk("rules/tnm_patterns.jsonl")

# Cargamos el dataset procesado
with open("data/processed/dataset.json", encoding="utf8") as f:
    records = [json.loads(line) for line in f]

#Evaluación
totales = {"T": 0, "N": 0, "M": 0, "Estadio": 0}
aciertos = {"T": 0, "N": 0, "M": 0, "Estadio": 0}
fallos = {"T": 0, "N": 0, "M": 0, "Estadio": 0}
nulos = {"T": 0, "N": 0, "M": 0, "Estadio": 0}

for r in records:
    doc = nlp(r["text"])
    extraido = {"T": None, "N": None, "M": None, "Estadio": None}

    for ent in doc.ents:
        if ent.label_ == "T_STAGE" and not extraido["T"]:
            extraido["T"] = ent.text
        elif ent.label_ == "N_STAGE" and not extraido["N"]:
            extraido["N"] = ent.text
        elif ent.label_ == "M_STAGE" and not extraido["M"]:
            extraido["M"] = ent.text
        elif ent.label_ == "ESTADIO" and not extraido["Estadio"]:
            extraido["Estadio"] = ent.text.replace(",", "").upper()

    for campo in ["T", "N", "M", "Estadio"]:
        esperado = (r[campo] or "").replace(",", "").upper().strip()
        predicho = (extraido[campo] or "").upper().strip()

        totales[campo] += 1
        if not predicho:
            nulos[campo] += 1
        elif predicho == esperado:
            aciertos[campo] += 1
        else:
            fallos[campo] += 1

# mostramos resultados
print("\n--- EVALUACIÓN DE EXTRACCIÓN ---")
for campo in ["T", "N", "M", "Estadio"]:
    print(f"\n🧪 Campo: {campo}")
    print(f"  Total                                               : {totales[campo]}")
    print(f"  Aciertos (extracción coincide con columna en excel) : {aciertos[campo]}")
    print(f"  Fallos  (extracción no coincide columna en excel)   : {fallos[campo]}")
    print(f"  No extraídos (No se extrajo nada)                   : {nulos[campo]}")
    exactitud = (aciertos[campo] / totales[campo]) * 100
    print(f"  ✅ Exactitud: {exactitud:.2f}%")