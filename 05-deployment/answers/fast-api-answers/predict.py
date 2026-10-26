import json
from typing import Any

from typing_extensions import Dict

from model import normalize_record

from pydantic import BaseModel

class Lead(BaseModel):
    lead_source: str | None = None
    industry: str | None = None
    employment_status: str | None = None
    location: str | None = None
    number_of_courses_viewed: int | None = None
    annual_income: float | None = None
    interaction_count: int | None = None
    lead_score: float | None = None

def predict(pipeline , candidate : Lead) -> dict[str , Any ] :
    rec = normalize_record(candidate.model_dump())
    first = float(pipeline.predict_proba([rec])[0, 1])
    second = float(pipeline.predict_proba([rec])[0, 1])

    assert 0 < first < 1
    assert first == second
    return {"conversion_probability": round(first, 6), "conversion": first >= 0.5}
