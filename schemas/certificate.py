from pydantic import BaseModel
from datetime import date, datetime

class Certificate(BaseModel):
    id: int
    code : int 
    broadcast_date: date
    autoridad_emisora: str # La autoridad o entidad responsable de emitir el certificado.
    type: str
    description: str # Una descripción o información adicional sobre el certificado.
    valid_until: date # La fecha de vencimiento o validez del certificado.
    created_by: str # El usuario que creó el certificado.
    state: str 
    
    
