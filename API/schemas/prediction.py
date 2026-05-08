"""
Esquemas de validación con Pydantic
"""
from pydantic import BaseModel, Field
from typing import List


class TumorFeatures(BaseModel):
    """Esquema para las características del tumor - 30 características exactas del dataset"""
    
    # Media de características (mean)
    radius_mean: float = Field(..., description="Radio medio")
    texture_mean: float = Field(..., description="Textura media")
    perimeter_mean: float = Field(..., description="Perímetro medio")
    area_mean: float = Field(..., description="Área media")
    smoothness_mean: float = Field(..., description="Suavidad media")
    compactness_mean: float = Field(..., description="Compacidad media")
    concavity_mean: float = Field(..., description="Concavidad media")
    concave_points_mean: float = Field(..., description="Puntos cóncavos medios")
    symmetry_mean: float = Field(..., description="Simetría media")
    fractal_dimension_mean: float = Field(..., description="Dimensión fractal media")
    
    # Error estándar (se)
    radius_se: float = Field(..., description="Radio - Error estándar")
    texture_se: float = Field(..., description="Textura - Error estándar")
    perimeter_se: float = Field(..., description="Perímetro - Error estándar")
    area_se: float = Field(..., description="Área - Error estándar")
    smoothness_se: float = Field(..., description="Suavidad - Error estándar")
    compactness_se: float = Field(..., description="Compacidad - Error estándar")
    concavity_se: float = Field(..., description="Concavidad - Error estándar")
    concave_points_se: float = Field(..., description="Puntos cóncavos - Error estándar")
    symmetry_se: float = Field(..., description="Simetría - Error estándar")
    fractal_dimension_se: float = Field(..., description="Dimensión fractal - Error estándar")
    
    # Peor valor (worst)
    radius_worst: float = Field(..., description="Radio - Peor valor")
    texture_worst: float = Field(..., description="Textura - Peor valor")
    perimeter_worst: float = Field(..., description="Perímetro - Peor valor")
    area_worst: float = Field(..., description="Área - Peor valor")
    smoothness_worst: float = Field(..., description="Suavidad - Peor valor")
    compactness_worst: float = Field(..., description="Compacidad - Peor valor")
    concavity_worst: float = Field(..., description="Concavidad - Peor valor")
    concave_points_worst: float = Field(..., description="Puntos cóncavos - Peor valor")
    symmetry_worst: float = Field(..., description="Simetría - Peor valor")
    fractal_dimension_worst: float = Field(..., description="Dimensión fractal - Peor valor")

    class Config:
        json_schema_extra = {
            "example": {
                "radius_mean": 17.99,
                "texture_mean": 10.38,
                "perimeter_mean": 122.8,
                "area_mean": 1001,
                "smoothness_mean": 0.1184,
                "compactness_mean": 0.2776,
                "concavity_mean": 0.3001,
                "concave_points_mean": 0.1471,
                "symmetry_mean": 0.2419,
                "fractal_dimension_mean": 0.07871,
                "radius_se": 1.095,
                "texture_se": 0.9053,
                "perimeter_se": 8.589,
                "area_se": 153.4,
                "smoothness_se": 0.006399,
                "compactness_se": 0.04904,
                "concavity_se": 0.05373,
                "concave_points_se": 0.01587,
                "symmetry_se": 0.03003,
                "fractal_dimension_se": 0.006193,
                "radius_worst": 25.38,
                "texture_worst": 17.33,
                "perimeter_worst": 184.6,
                "area_worst": 2019,
                "smoothness_worst": 0.162,
                "compactness_worst": 0.6656,
                "concavity_worst": 0.7119,
                "concave_points_worst": 0.2654,
                "symmetry_worst": 0.4601,
                "fractal_dimension_worst": 0.11890
            }
        }


class PredictionResponse(BaseModel):
    """Esquema para la respuesta de predicción"""
    
    diagnosis: str = Field(..., description="Diagnóstico (Maligno o Benigno)")
    probability: float = Field(..., description="Probabilidad de la predicción")
    confidence: str = Field(..., description="Nivel de confianza")
    
    class Config:
        json_schema_extra = {
            "example": {
                "diagnosis": "Maligno",
                "probability": 0.95,
                "confidence": "Muy Alto"
            }
        }


class ErrorResponse(BaseModel):
    """Esquema para respuestas de error"""
    
    error: str = Field(..., description="Mensaje de error")
    detail: str = Field(None, description="Detalles adicionales")
