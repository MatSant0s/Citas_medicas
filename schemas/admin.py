from pydantic import BaseModel
import datetime

class Admin(BaseModel):
    id: int
    name: str
    lastname: str
    email: str
    phone: int
    role: str
    creation_date: datetime
    last_connection: datetime
    permissions: str
    assigned_doctors: str
    assigned_patients: str
    activity_logs: str