from pydantic import BaseModel
import datetime

class Assistant(BaseModel):
    id: int
    gender: str
    name: str
    lastname: str
    phone: int
    supervisor_name: str
    email: str
    admin: str # Una instancia de la clase "Admin" que representa la conexión directa con el administrador.
    assigned_tasks: str # Una lista de las tareas asignadas al asistente por el administrador.
    available_time: datetime # El horario disponible del asistente para realizar tareas.
    last_connection: datetime # La fecha y hora de la última conexión del asistente al sistema.
    permissions: str # Un conjunto de los permisos o privilegios asignados al personal de apoyo por el administrador.
    completed_tasks: str #Un conjunto de las tareas completadas por el personal de apoyo.
    activity_records: str #Un conjunto de los registros o actividades realizadas por el personal de apoyo en el sistema.
