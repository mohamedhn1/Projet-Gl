from pydantic import BaseModel
from typing import List

class LawyerSignUp(BaseModel):
    name:str
    email:str  
    specialty :str
    phone_number :str
    office_address :str
    website :str
    linkedin_profile :str
    wilaya:str
    password:str
    class config():
     orm_mode = True


class LawyerDetails(BaseModel):
    competence:str
    experience:str
    domaine_de_pratique:str
    


class login(BaseModel):
    email:str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None
    scopes: list[str] = []

