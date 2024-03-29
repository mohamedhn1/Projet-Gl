from fastapi import APIRouter, Depends
from ..database import database
from sqlalchemy.orm import Session
from ..repositories.search import usersearch as usersr
""", adminsearch as adminsr"""

router = APIRouter(prefix="/search", tags=["Search"])

@router.get("/search")
def search(name:str = '',wilaya:str = '',categories:str = '',page:int = 1,limit:int = 25,db:Session=Depends(database.get_db)):
    searchResult = usersr(name,wilaya,categories,page,limit,db)
    if(searchResult != None):
        return {"result":searchResult}
    else :
        return {"result":"No results found"}

"""
@router.get("/adminsearch")
def adminsearch(name:str = '',wilaya:str = '',categories:str = '',status:str ='accepted',isBlocked:bool = False,page:int = 1,limit:int = 25,db:Session=Depends(get_db)):
    searchResult = adminsr(name,wilaya,categories,page,limit,db)
    if(searchResult != None):
        return {"result":searchResult}
    else :
        return {"result":"No results found"}"""