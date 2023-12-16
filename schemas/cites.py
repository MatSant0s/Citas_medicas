from pydantic import BaseModel
from datetime import date, datetime, time
from typing import List, Union
import uuid

class Cites(BaseModel):
    query_type: str
    query_description: str
    site: str
    number_cite: str
    consulting_room: str
    horary: datetime
    id_pacient: int
    id_medic: int
    state: str 
    admin: Union[int, None] 
    assistant: Union[int, None] 
    observations: str 
    reminder_sent: bool 
    register_by: Union[int, None] 
    class Config:
        schema_extra = {
            "example": {
                "query_type" : "Unknown",
                "query_description": "Content of the query",
                "site": "Centro de Salud",
                "number_cite": str(uuid.uuid4()),
                "consulting_room": "2A",
                "horary": "2009-12-07 10:00:00",
                "id_pacient": 1,
                "id_medic": 1,
                "state": "Agendada",
                "admin": None,
                "assistant": None,
                "observations": "Observations to do after the cite",
                "reminder_sent": False,
                "register_by": None
            }
        }

class ListCites(BaseModel):
    cites: List[Cites]

class UpdateCite(BaseModel):
    id_cite: int
    query_type: str
    query_description: str
    site: str
    consulting_room: str
    horary: datetime
    id_pacient: int
    id_medic: int 
    state: str
    admin: Union[int, None]
    assistant: Union[int, None]
    observations: str 
    reminder_sent: bool 
    register_by: Union[int, None] 
    
    class Config:
        schema_extra = {
            "example": {
                "id_cite": 1,
                "query_type" : "Unknown",
                "query_description": "Content of the query",
                "site": "Centro de Salud",
                "consulting_room": "2A",
                "horary": "2009-12-07 10:00:00",
                "id_pacient": 1,
                "id_medic": 1,
                "state": "Agendada",
                "admin": None,
                "assistant": None,
                "observations": "Observations to do after the cite",
                "reminder_sent": False,
                "register_by": None             
            }
        }
