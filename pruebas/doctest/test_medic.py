from src.config.database import Session, engine, Base
from src.models.medic import Medic as MedicModel
from src.schemas.medic import Medic, UpdateMedic
from fastapi.responses import JSONResponse
from fastapi import status
from fastapi.encoders import jsonable_encoder

Base.metadata.create_all(bind= engine)

#----------------------------------------------------------------------------------------------------
def get_medic(medic_id: int):
    """
    Función que obtiene un médico por su ID.

    Args:
        medic_id (int): El ID del médico.

    Returns:
        JSONResponse: Un objeto JSONResponse con el resultado de la consulta.

    >>> get_medic(1)
    JSONResponse(status_code=200, content={'id_medic': 1})
    
    >>> get_medic(999)
    JSONResponse(status_code=404, content={'message': 'Medic not Found'})
    """
    """
    db = Session()
    res = db.query(MedicModel).filter(MedicModel.id_medic == medic_id).first()

    if not res:
        return JSONResponse(status_code= status.HTTP_404_NOT_FOUND,
                content= {"message": "Medic not Found"})                        
    
    return JSONResponse(status_code= status.HTTP_200_OK, content= jsonable_encoder(res))
    """

#----------------------------------------------------------------------------------------------------
def get_all_medic():
    """
    Función que obtiene todos los médicos.

    Returns:
        JSONResponse: Un objeto JSONResponse con el resultado de la consulta.

    >>> get_all_medic()
    JSONResponse(status_code=200, content=[{'id': 1, 'name': 'Mateo Santos'}, {'id': 2, 'name': 'Juan Perez'}])
    """
    """
    db = Session()
    res = db.query(MedicModel).all()

    return JSONResponse(status_code= status.HTTP_200_OK,
                        content= jsonable_encoder(res))
    """

#----------------------------------------------------------------------------------------------------
def create_medic(medic: Medic):
    """
    Función que crea un nuevo médico.

    Args:
        medic (Medic): Un objeto de tipo Medic con los datos del médico a crear.

    Returns:
        Dict: Un diccionario con los datos del médico creado.

    >>> create_medic(Medic(name="Mateo Santos", specialty="Cardiology"))
    {'name': 'Juan Perez', 'specialty': 'Cardiology'}
    """
    """
    db = Session()
    new_medic = MedicModel(**medic.dict())

    db.add(new_medic)
    db.commit()

    return medic.dict()
    """
    
