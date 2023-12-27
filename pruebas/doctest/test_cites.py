from src.config.database import Session, engine, Base
from src.models.cites import Cites as CiteModel
from src.schemas.cites import Cites, ListCites, UpdateCite
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import status

Base.metadata.create_all(bind= engine)

#----------------------------------------------------------------------------------------------------
def get_cite_by_id(id_cite: int):
    """
    Función que obtiene una cita por su ID.

    Args:
        id_cite (int): El ID de la cita.

    Returns:
        JSONResponse: Un objeto JSONResponse con el resultado de la consulta.

    >>> get_cite_by_id(1)
    JSONResponse(status_code=200, content={'id_cite': 1})
    
    >>> get_cite_by_id(999)
    JSONResponse(status_code=404, content={'message': 'Cite not Found'})
    """
    """
    db = Session()
    res = db.query(CiteModel).filter(CiteModel.id_cite == id_cite).first()

    if not res:
        return JSONResponse(status_code= status.HTTP_404_NOT_FOUND,
                    content= {"message": "Cite not Found"})         

    return JSONResponse(status_code= status.HTTP_200_OK, content= jsonable_encoder(res))
    """

#----------------------------------------------------------------------------------------------------
def get_cite_by_patient_id(id_pacient: int):
    """
    Función que obtiene una cita por el ID del paciente.

    Args:
        id_pacient (int): El ID del paciente.

    Returns:
        JSONResponse: Un objeto JSONResponse con el resultado de la consulta.

    >>> get_cite_by_patient_id(1)
    JSONResponse(status_code=200, content={'id_pacient': 1})
    
    >>> get_cite_by_patient_id(999)
    JSONResponse(status_code=404, content={'message': 'Cite not Found'})
    """
    """
    db = Session()
    res = db.query(CiteModel).filter(CiteModel.id_pacient == id_pacient).first()

    if not res:
        return JSONResponse(status_code= status.HTTP_404_NOT_FOUND,
                    content= {"message": "Cite not Found"})  
    
    return JSONResponse(status_code= status.HTTP_200_OK, content= jsonable_encoder(res))
    """

