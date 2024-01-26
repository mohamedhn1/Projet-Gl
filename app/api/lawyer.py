
from fastapi import APIRouter,Depends,status,HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from ..models import models
from ..schemas import schemas
from ..database import database
from ..repositories import lawyer
from sqlalchemy.orm import Session
from typing import List

from ..repositories.hashing import Hash
from .. import token


router=APIRouter(tags=['account'],prefix='/lawyer_account')

@router.post('/login')
def login(request:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(database.get_db)):
   lawyer=db.query(models.Lawyer).filter(models.Lawyer.email==request.username).first()
   if not lawyer :
      raise HTTPException (status_code=status.HTTP_404_NOT_FOUND,detail=f"invalid credentials")
   if not lawyer.password == request.password:
      raise HTTPException (status_code=status.HTTP_404_NOT_FOUND,detail=f"incorrect password")

   access_token = token.create_access_token(
        data={"sub": lawyer.email} )
   return {"access_token": access_token, "token_type": "bearer"}

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






    



 
