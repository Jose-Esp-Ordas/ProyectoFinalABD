"""
Configuración del proyecto
"""
import os
from pathlib import Path

# Rutas
PROJECT_DIR = Path(__file__).parent.parent
DATA_DIR = PROJECT_DIR / "data"
MODELS_DIR = PROJECT_DIR / "modelos"

# Archivos
MODEL_PATH = MODELS_DIR / "best_model.joblib"
SCALER_PATH = MODELS_DIR / "scaler.joblib"

# Configuración de datos
TARGET_COLUMN = "diagnosis"
ID_COLUMN = "id"
FEATURES_TO_REMOVE = [ID_COLUMN, TARGET_COLUMN]

# Configuración del modelo
TEST_SIZE = 0.2
RANDOM_STATE = 42
