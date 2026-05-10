"""
Rutas para predicciones
"""
from fastapi import APIRouter, HTTPException
import joblib
import pandas as pd
from schemas.prediction import TumorFeatures, PredictionResponse, ErrorResponse
from config import MODEL_PATH, SCALER_PATH


router = APIRouter(prefix="/predict", tags=["predictions"])

# Variables globales para el modelo y scaler
model = None
scaler = None


def load_model_and_scaler():
    """Carga el modelo y el scaler"""
    global model, scaler
    try:
        model = joblib.load(MODEL_PATH)
        scaler = joblib.load(SCALER_PATH)
        print("✓ Modelo y scaler cargados")
    except FileNotFoundError:
        print("Modelo o scaler no encontrado")


@router.post("/predict", response_model=PredictionResponse)
async def predict(features: TumorFeatures):
    """
    Predice el diagnóstico del tumor a partir de las características
    
    - **diagnosis**: Maligno (M) o Benigno (B)
    - **probability**: Confianza de la predicción (0-1)
    - **confidence**: Nivel de confianza interpretado
    """
    
    if model is None or scaler is None:
        raise HTTPException(
            status_code=500,
            detail="Modelo no cargado. Verifique que los archivos existan."
        )
    
    try:
        # Convertir características a DataFrame
        features_dict = features.model_dump()
        df_features = pd.DataFrame([features_dict])
        
        # Escalar características
        features_scaled = scaler.transform(df_features)
        
        # Hacer predicción
        prediction = model.predict(features_scaled)[0]
        probability = model.predict_proba(features_scaled)[0]
        
        # Mapear predicción
        diagnosis_map = {0: "Benigno", 1: "Maligno"}
        diagnosis = diagnosis_map[prediction]
        
        # Obtener probabilidad máxima
        prob_max = max(probability)
        
        # Determinar confianza
        if prob_max >= 0.9:
            confidence = "Muy Alto"
        elif prob_max >= 0.75:
            confidence = "Alto"
        elif prob_max >= 0.6:
            confidence = "Medio"
        else:
            confidence = "Bajo"
        
        return PredictionResponse(
            diagnosis=diagnosis,
            probability=float(prob_max),
            confidence=confidence
        )
    
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Error en la predicción: {str(e)}"
        )


@router.get("/health")
async def health_check():
    """
    Verifica el estado de la API
    """
    return {
        "status": "healthy",
        "model_loaded": model is not None,
        "scaler_loaded": scaler is not None
    }
