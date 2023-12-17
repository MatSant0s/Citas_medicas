from datetime import date, datetime
from pydantic import BaseModel
from typing import List

class Pacient(BaseModel):
    name: str
    lastname: str
    gender: str
    weight: float
    height: float
    ethnicity: str
    allergies: str
    HTA: int 
    cie_code: int
    birthday: date     
    blood_type: str
    address: str
    phone: int

    class Config:
        schema_extra = {
            "example": {
                    "name": "Tobias",
                    "lastname": "Tello",
                    "gender": "Male",
                    "weight": 70,
                    "height": 1.70,
                    "ethnicity": "Caucasica",
                    "allergies": "Polvo",
                    "HTA": 110, 
                    "cie_code": 544556,
                    "birthday": "2002-07-11",    
                    "blood_type": "A+",
                    "address": "Chimbacalle",
                    "phone": "0107444457"
            }
        }

class ListPacient(BaseModel):
    pacients: List[Pacient]
    
class UpdatePacient(BaseModel):
    id: int
    gender: str
    name: str
    lastname: str
    weight: float
    height: float
    ethnicity: str
    allergies: str
    HTA: int 
    cie_code: int
    birthday: date     
    blood_type: str
    address: str
    phone: int

    class Config:
        schema_extra = {
            "example": {
                    "id": 1,
                    "name": "Dilan",
                    "lastname": "Maigua",
                    "gender": "Male",
                    "weight": 75,
                    "height": 1.75,
                    "ethnicity": "Afroecuatoriana",
                    "allergies": "None",
                    "HTA": 110, 
                    "cie_code": 456563,
                    "birthday": "2003-01-07" ,    
                    "blood_type": "O+",
                    "address": "Machachi",
                    "phone": "0995993021"
            }
        }