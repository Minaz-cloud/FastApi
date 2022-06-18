from fastapi import APIRouter, Depends,status
from typing import List
from sqlalchemy.orm import Session
from .. import schemas,database
from ..repository import bankmaster

router = APIRouter(
    prefix= '/bankmaster',
    tags=['BankMaster']
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.BankBaseUpdate, db:Session= (Depends(database.get_db))): #,current_user:schemas.UserTest=Depends(oauth2.get_current_user)):
    return bankmaster.create(request,db)


@router.get('/', response_model=List[schemas.Bank])
#def all(db:Session = Depends(database.get_db),current_user:schemas.UserTest=Depends(oauth2.get_current_user)):
def all(db:Session = Depends(database.get_db)):
    return bankmaster.get_all(db)


@router.get('/{id}', status_code=200, response_model=schemas.Bank)
#def show(request: schemas.Stat,db:Session = Depends(database.get_db),current_user:schemas.UserTest=Depends(oauth2.get_current_user)):
def show(id:int,db:Session = Depends(database.get_db)):
    return bankmaster.show(id,db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)#, response_model=schemas.BankBaseUpdate)
def update(id:int, request:schemas.BankBaseUpdate, db:Session = Depends(database.get_db)): #,current_user:schemas.UserTest=Depends(oauth2.get_current_user)):
    return bankmaster.update(id,request,db)


@router.delete('/{id}')#, status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int, db:Session = Depends(database.get_db)): #,current_user:schemas.UserTest=Depends(oauth2.get_current_user)):
    return bankmaster.delete(id, db)
