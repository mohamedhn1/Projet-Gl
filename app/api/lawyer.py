from fastapi import APIRouter,Depends
from ..schemas import schemas
from ..database import database
from ..repositories import lawyer
from sqlalchemy.orm import Session


router=APIRouter(tags=['account'],prefix='/lawyer_account')

@router.post('/create')
def create_lawyer(request:schemas.LawyerSignUp ,db:Session = Depends(database.get_db)):
    return lawyer.create_lawyer(request,db)
   





    



 
