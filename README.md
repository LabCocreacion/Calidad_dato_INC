# Proyecto de Calidad de Datos - Extracción TNM y Estadificación Oncológica

## 📖 Descripción

Este proyecto implementa un sistema de **Procesamiento de Lenguaje Natural (NLP)** para la **extracción automática de información oncológica** desde textos médicos. Se enfoca específicamente en identificar y extraer:

- **Clasificación TNM** (Tumor, Nodos, Metástasis)
- **Estadificación clínica** de cáncer
- **Información estructurada** desde descripciones médicas no estructuradas

El objetivo es mejorar la **calidad de los datos oncológicos** mediante la automatización de la extracción de información crítica desde documentos médicos.

## 🏗️ Estructura del Proyecto

```
nlp_estadio_project/
├── README.md
├── requirements.txt
├── config/
│   └── config.cfg
├── data/
│   ├── raw/
│   │   └── descarga_calidad_datos_purgada.xlsx
│   └── processed/
│       └── dataset.json
├── models/
├── notebooks/
├── rules/
│   ├── tnm_patterns.jsonl
│   └── tnm_patterns_documentado.jsonl
└── scripts/
    ├── 01_preprocess_excel.py
    ├── 02_entityruler_test.py
    └── 03_measure_extraction.py
```

## 🔧 Instalación

### Prerrequisitos
- Python 3.8+
- pip

### Configuración del entorno

```bash
# Clonar el repositorio
git clone https://github.com/LabCocreacion/Calidad_dato_INC.git
cd Calidad_dato_INC/nlp_estadio_project

# Instalar dependencias
pip install -r requirements.txt
```

### Dependencias principales
- **spaCy 3.8.7**: Framework principal de NLP
- **pandas**: Manipulación de datos
- **numpy**: Cálculos numéricos
- **openpyxl**: Lectura de archivos Excel (implícita)

## 🚀 Uso

### 1. Preprocesamiento de datos
Convierte el archivo Excel de entrada en formato JSON estructurado:

```bash
python scripts/01_preprocess_excel.py
```

**Input**: `data/raw/descarga_calidad_datos_purgada.xlsx`  
**Output**: `data/processed/dataset.json`

### 2. Prueba de extracción con reglas
Prueba las reglas de extracción en una muestra de datos:

```bash
python scripts/02_entityruler_test.py
```

### 3. Evaluación completa
Ejecuta la evaluación automática en todo el dataset:

```bash
python scripts/03_measure_extraction.py
```

## 📊 Funcionalidades

### Extracción de Entidades

El sistema identifica automáticamente:

| Entidad | Descripción | Ejemplos |
|---------|-------------|----------|
| **T_STAGE** | Tamaño del tumor | T1, T2, T3, T4 |
| **N_STAGE** | Afectación de nodos linfáticos | N0, N1, N2, N3 |
| **M_STAGE** | Presencia de metástasis | M0, M1, Mx |
| **ESTADIO** | Estadificación clínica | I, II, III, IV |

### Patrones de Reconocimiento

- **Expresiones regulares avanzadas** para identificar patrones TNM
- **Reglas contextuales** para estadificación clínica
- **Normalizacion automática** de formatos de texto

## 📈 Métricas de Evaluación

El sistema proporciona métricas automáticas de:
- **Precisión** por tipo de entidad
- **Cobertura** de extracción
- **Casos nulos** identificados
- **Análisis de fallos** detallado

## 🔍 Configuración de Reglas

Las reglas de extracción se encuentran en:
- `rules/tnm_patterns.jsonl`: Patrones de producción
- `rules/tnm_patterns_documentado.jsonl`: Patrones documentados

### Ejemplo de regla:
```json
{
  "label": "T_STAGE", 
  "pattern": [{"TEXT": {"REGEX": "^T[0-4][a-b]?$"}}]
}
```

## 📋 Formato de Datos

### Entrada (Excel)
```
| Enfermedad | Motivo Atención | Observación | T | N | M | Est |
|------------|-----------------|-------------|---|---|---|-----|
| Carcinoma  | Seguimiento     | T2N0M0      |T2 |N0 |M0 | II  |
```

### Salida (JSON)
```json
{
  "text": "Carcinoma Seguimiento T2N0M0",
  "T": "T2",
  "N": "N0", 
  "M": "M0",
  "Estadio": "II"
}
```

## 🛠️ Desarrollo

### Agregar nuevos patrones
1. Editar `rules/tnm_patterns.jsonl`
2. Ejecutar `02_entityruler_test.py` para probar
3. Evaluar con `03_measure_extraction.py`

### Estructura de directorios
- `config/`: Archivos de configuración
- `data/raw/`: Datos originales
- `data/processed/`: Datos procesados
- `models/`: Modelos entrenados (futuro)
- `notebooks/`: Jupyter notebooks para análisis
- `rules/`: Reglas de extracción
- `scripts/`: Scripts de procesamiento

## 📝 Licencia

Este proyecto es desarrollado por **LabCocreacion** para mejorar la calidad de datos en oncología.

## 🤝 Contribuir

1. Fork el proyecto
2. Crear rama de feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit cambios (`git commit -am 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crear Pull Request

## 📞 Contacto

**LabCocreacion**  
Proyecto: Calidad de Datos INC
