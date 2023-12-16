from pydantic import BaseModel
from datetime import date, datetime

class Consultation(BaseModel):
    date: date 
    hour: datetime
    patient: str
    medic: str
    reason: str
    diagnosis: str
    treatment: str
    recipe: str
    observations: str
    registered_by: str

    
    
    