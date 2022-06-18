from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from .. import schemas,database
from ..repository import merchant
from typing import List

router = APIRouter(
    prefix= '/merchant',
    tags=['Merchant']
)

'''@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Merchant, db:Session= (Depends(database.get_db)),current_user:schemas.UserTest=Depends(oauth2.get_current_user)):
    return merchant.create(db,request)
'''


@router.get('/', response_model=List[schemas.MerchantBase])
#def all(db:Session = Depends(database.get_db),current_user:schemas.UserTest=Depends(oauth2.get_current_user)):
def all(db:Session = Depends(database.get_db)):
    return merchant.get_all(db)

@router.get('/{id}', status_code=200, response_model=schemas.MerchantBase)
#def show(request: schemas.Stat,db:Session = Depends(database.get_db),current_user:schemas.UserTest=Depends(oauth2.get_current_user)):
def show(id:int,db:Session = Depends(database.get_db)):
    return merchant.show(id,db)


@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED, response_model=schemas.MerchantUpdate)
def update(id:int, request:schemas.MerchantUpdate, db:Session = Depends(database.get_db)): #,current_user:schemas.UserTest=Depends(oauth2.get_current_user)):
    return merchant.update(id,db,request)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int, db:Session = Depends(database.get_db)): #,current_user:schemas.UserTest=Depends(oauth2.get_current_user)):
    return merchant.delete(id, db)