import unittest
from unittest.mock import patch, MagicMock, Mock

from fastapi.responses import JSONResponse
from fastapi import status
from fastapi.encoders import jsonable_encoder

from src.config.database import Session
from src.models.cites import Cites as CiteModel
from src.schemas.cites import Cites, UpdateCite
from src.services.cites import (
    get_cite_by_id,
    get_cite_by_patient_id,
    get_cites_by_medic_id,
    create_cite,
    patch_cite,
    delete_cite,
)


def get_all_cites():
    db = Session()
    res = db.query(CiteModel).all()

    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(res))


