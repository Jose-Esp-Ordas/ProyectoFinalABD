# Proyecto: Clasificación de Tumores de Mama

## Descripción

Sistema completo de clasificación de tumores de mama (malignos/benignos) implementando:

- **Etapa I**: Análisis y preprocesamiento de datos
- **Etapa II**: Desarrollo y comparación de modelos ML
- **Etapa III**: API REST con FastAPI

## Iniciación

### 1. Clonar el repositorio

```bash
git clone <URL-REPOSITORIO>
cd ProyectoABD
```

### 2. Crear entorno virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# o
venv\Scripts\activate     # Windows
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### Ejecutar Jupyter Notebook

```bash
jupyter notebook notebooks/01_analisis_preprocesamiento.ipynb
```

### Iniciar servidor API

```bash
python -m uvicorn src.main:app --reload
```

### Acceder a documentación

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Endpoints disponibles

#### 1. Health Check

```bash
GET /api/health
```

#### 2. Predicción

```bash
POST /api/predict
Content-Type: application/json

{
  "radius_mean": 17.99,
  "texture_mean": 10.38,
  "perimeter_mean": 122.8,
  "area_mean": 1001,
  "smoothness_mean": 0.1184,
  ...
}
```

**Respuesta:**

```json
{
  "diagnosis": "Maligno",
  "probability": 0.95,
  "confidence": "Muy Alto"
}
```
