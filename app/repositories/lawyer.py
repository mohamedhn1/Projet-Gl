from fastapi import APIRouter,Depends,status,HTTPException
from ..schemas import schemas
from ..models import models
from ..database import database
from typing import List
from sqlalchemy.orm import Session
from . import hashing




def create_lawyer(request:schemas.LawyerSignUp,db:Session = Depends(database.get_db),):
    newLawyer = models.Lawyer(name=request.name,
                              email=request.email,
                              specialty=request.specialty,
                              phone_number=request.phone_number,
                              office_address=request.office_address,
                              website=request.website,
                              linkedin_profile=request.linkedin_profile,
                              wilaya=request.wilaya,
                              password=hashing.Hash.bcrypt(request.password),
                                                                                )
    db.add(newLawyer)
    db.commit()
    db.refresh(newLawyer)
    return newLawyer













    """""

def get_lawyer_details(id:int,db:Session = Depends(database.get_db)):
    lawyer=db.query(models.Lawyer).get(id)
    lawyer_details = db.query(models.Lawyer_details).get(id)
    if lawyer and lawyer_details:
        # Return a dictionary with lawyer details
        return {
            'lawyer_id': lawyer.id,
            'name': lawyer.name,
            'additional_attribute': lawyer_details.additional_attribute1,
            # Add more key-value pairs for other attributes as needed
        }
    else:
        # Return None or raise an exception based on your preference
        return 'helloo'



"""

def read_avocats(db: Session, skip: int = 0, limit: int = 10):
    avocats = db.query(models.Lawyer).offset(skip).limit(limit).all()
    return avocats
def read_avocat(avocat_id: int, db: Session):
    avocat = db.query(models.Lawyer).filter(models.Lawyer.id == avocat_id).first()
    if avocat is None:
        raise HTTPException(status_code=404, detail="Avocat non trouvé")
    return avocat
def read_avocatname(avocat_name: str, db: Session):
    avocat = db.query(models.Lawyer).filter(models.Lawyer.name == avocat_name).first()
    if avocat is None:
        raise HTTPException(status_code=404, detail="Avocat non trouvé avec ce nom")
    return avocat