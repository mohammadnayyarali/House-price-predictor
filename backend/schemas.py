from pydantic import BaseModel, Field, conint, confloat

class PredictionRequest(BaseModel):
    area: confloat(gt=0)
    bedrooms: conint(ge=0, le=10)
    bathrooms: confloat(gt=0, le=10)
    year_built: conint(ge=1800, le=2026)
    garage: conint(ge=0, le=5)
    lot_size: confloat(gt=0)
    location: str = Field(..., min_length=2, max_length=50)

class PredictionResult(BaseModel):
    price: float
