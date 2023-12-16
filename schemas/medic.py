from pydantic import BaseModel
from datetime import date, datetime, time
from typing import List, Union

class Medic(BaseModel):
    cedula: int
    name: str
    lastname: str
    gender: str
    speciality: str
    phone: int
    email: str
    address: str
    schedule_start: time #
    schedule_end: time
    experience: int
    certifications: Union[int, None]
    
    
    class Config:
        schema_extra = {
            "example": {
                    "cedula": 107444457,
                    "name": "Tobias",
                    "lastname": "Tello",
                    "gender": "Male",
                    "speciality": "Ginecologia",
                    "phone": "0993994020",
                    "email": "tobiastello2002@gmail.com",
                    "address": "Chimbacalle", 
                    "schedule_start": "08:00:00",
                    "schedule_end": "16:00:00",
                    "experience": 2,
                    "certifications": None,
            }
        } 


class ListMedic(BaseModel):
    medics: List[Medic]
    
class UpdateMedic(BaseModel):
    id: int
    cedula: int
    name: str
    lastname: str
    gender: str
    speciality: str
    phone: int
    email: str
    address: str
    schedule_start: time 
    schedule_end: time
    experience: int 
    certifications: Union[int, None]
    
    class Config:
        schema_extra = {
            "example": {
                    "id": 1,
                    "cedula": 1304427071,
                    "name": "Mateo",
                    "lastname": "Santos",
                    "gender": "Male",
                    "speciality": "Obstetricia",
                    "phone": "0992271348",
                    "email": "santosmateoo21@gmail.com",
                    "address": "Chimbacalle", 
                    "schedule_start": "08:00:00",
                    "schedule_end": "16:00:00",
                    "experience": 3,
                    "certifications": None,
            }
        } 
