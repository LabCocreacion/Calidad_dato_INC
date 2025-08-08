#Aplicar patrones simples (regex) para detectar T, N, M y Estadio directamente desde el texto

import spacy
from spacy.pipeline import EntityRuler
import json

nlp = spacy.blank("es")
ruler = nlp.add_pipe("entity_ruler")
ruler.from_disk("rules/tnm_patterns.jsonl")

with open("data/processed/dataset.json", encoding="utf8") as f:
    lines = [json.loads(line) for line in f]

# Probar sobre los primeros 10
for ex in lines[:10]:
    doc = nlp(ex["text"])
    print("TEXTO:", ex["text"][:150], "...")
    for ent in doc.ents:
        print(f"  - {ent.label_}: {ent.text}")
    print("VERDADERO:", f"T={ex['T']}, N={ex['N']}, M={ex['M']}, Estadio={ex['Estadio']}")
    print("---")