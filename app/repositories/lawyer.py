from fastapi import APIRouter,Depends,status,HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from ..schemas import schemas
from ..models import models
from ..database import database
from typing import List
from sqlalchemy.orm import Session
from . import hashing




def create_lawyer(request:schemas.LawyerSignUp,db:Session = Depends(database.get_db)):
    newLawyer = models.Lawyer(name=request.name,
                              email=request.email,
                              specialty=request.specialty,
                              phone_number=request.phone_number,
                              office_address=request.office_address,
                              website=request.website,
                              linkedin_profile=request.linkedin_profile,
                              wilaya=request.wilaya,
                              categories = request.categories,
                              password=request.password,
                              cordoneex=request.cordoneex,
                              cordoneey=request.cordoneey
                              
                                                                                )
    db.add(newLawyer)
    db.commit()
    db.refresh(newLawyer)
    return newLawyer

def login_lawyer(db: Session,request:OAuth2PasswordRequestForm ):
    lawyer=db.query(models.Lawyer).filter(models.Lawyer.email==request.username).first()
    return lawyer

def delete_lawyer(db:Session,lawyerid:int):
    lawyer = db.query(models.Lawyer).filter(models.Lawyer.id==lawyerid)
    if not lawyer.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Lawyer not found")
    lawyerratings = db.query(models.Rating).filter(models.Rating.lawyerId == lawyer.first().id)
    lawyerratings.delete(synchronize_session = False)
    lawyer.delete(synchronize_session = False)
    db.commit()
    return lawyerid
    

def read_avocats(db: Session, skip: int = 0, limit: int = 10):
    avocats = db.query(models.Lawyer).offset(skip).limit(limit).all()
    return avocats
def get_by_id(avocat_id: int, db: Session):
    avocat = db.query(models.Lawyer).filter(models.Lawyer.id == avocat_id).first()
    if avocat is None:
        raise HTTPException(status_code=404, detail="Avocat non trouvé")
    return avocat
def read_avocatname(avocat_name: str, db: Session):
    avocat = db.query(models.Lawyer).filter(models.Lawyer.name == avocat_name).first()
    if avocat is None:
        raise HTTPException(status_code=404, detail="Avocat non trouvé avec ce nom")
    return avocat