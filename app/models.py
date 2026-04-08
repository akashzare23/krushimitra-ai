from pydantic import BaseModel
from typing import Optional


class FarmState(BaseModel):
    day: int
    season: str
    soil_type: str
    soil_moisture: float
    temperature: float
    humidity: float
    rain_forecast_3d: float
    rain_forecast_7d: float
    tank_level: float
    water_availability: str
    crop_stage: str
    selected_crop: Optional[str] = None
    crop_health: float = 50.0


class AgentAction(BaseModel):
    crop_choice: Optional[str] = None
    sow_now: Optional[bool] = None
    irrigate: Optional[bool] = None
    water_amount: Optional[float] = 0.0


class StepResponse(BaseModel):
    state: FarmState
    reward: float
    done: bool
    info: dict = {}