from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from .. import schemas,database
from ..repository import merchant_limit

router = APIRouter(
    prefix= '/merchant_limit',
    tags=['MerchantLimit']
)

@router.post('/{id}', status_code=status.HTTP_201_CREATED)
def create(id:int, request: schemas.MerchantLimit, db:Session= (Depends(database.get_db))):#,current_user:schemas.UserTest=Depends(oauth2.get_current_user)):
    return merchant_limit.create(id,db,request)

@router.get('/{id}', status_code=200, response_model=schemas.MerchantLimitCurd)
#def show(request: schemas.Stat,db:Session = Depends(database.get_db),current_user:schemas.UserTest=Depends(oauth2.get_current_user)):
def show(id:int,db:Session = Depends(database.get_db)):
    return merchant_limit.show(id,db)


@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request:schemas.MerchantLimitCurd, db:Session = Depends(database.get_db)): #,current_user:schemas.UserTest=Depends(oauth2.get_current_user)):
    return merchant_limit.update(id,db,request)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int, db:Session = Depends(database.get_db)): #,current_user:schemas.UserTest=Depends(oauth2.get_current_user)):
    return merchant_limit.delete(id, db)