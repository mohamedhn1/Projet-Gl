from sqlalchemy import Column, Integer, String,ForeignKey
from ..database.database import Base
from sqlalchemy.orm import relationship





class Lawyer(Base):
    __tablename__='lawyers'
    id=Column(Integer,primary_key=True,index=True,autoincrement=True)
    name=Column(String)
    email=Column(String,unique=True)    
    specialty = Column(String)
    phone_number = Column(String)
    office_address = Column(String)
    website = Column(String)
    linkedin_profile = Column(String)
    wilaya=Column(String)
    password=Column(String)    
    details = relationship("Lawyer_details")


class Lawyer_details(Lawyer):
    __tablename__ = 'lawyer_details'
    lawyer_id = Column(Integer, ForeignKey('lawyers.id'), primary_key=True)
    competence = Column(String)
    experience = Column(String)
    domaine_de_pratique=Column(String)
    lawyer = relationship("Lawyer")

    







