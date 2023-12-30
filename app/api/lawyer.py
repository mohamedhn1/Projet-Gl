from fastapi import APIRouter,Depends
from ..schemas import schemas
from ..database import database
from ..repositories import lawyer
from sqlalchemy.orm import Session
from typing import List

router=APIRouter(tags=['account'],prefix='/lawyer_account')

@router.post('/create')
def create_lawyer(request:schemas.LawyerSignUp ,db:Session = Depends(database.get_db)):
    return lawyer.create_lawyer(request,db)
   
# Endpoint pour obtenir la liste de tous les avocats
@router.get("/avocats/infos", response_model=List[schemas.LawyerSignUp])
async def read_avocats(db: Session = Depends(database.get_db), skip: int = 0, limit: int = 10):
    avocats = lawyer.read_avocats(db=db, skip=skip, limit=limit)
    return avocats

# Endpoint pour obtenir le profil détaillé d'un avocat par son ID
@router.get("/avocats/infos/{avocat_id}", response_model=schemas.LawyerSignUp)
def read_avocat(avocat_id: int, db: Session = Depends(database.get_db)):
    return lawyer.read_avocat(avocat_id=avocat_id,db=db)


@router.get("/avocats/infos/{avocat_name}", response_model=schemas.LawyerSignUp)
def read_avocatname(avocat_name: str, db: Session = Depends(database.get_db)):
    return lawyer.read_avocatname(avocat_name=avocat_name,db=db)





    



 
