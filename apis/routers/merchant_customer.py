from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from .. import schemas,database
from ..repository import merchant_customer
from typing import List

router = APIRouter(
    prefix= '/merchant_customer',
    tags=['MerchantCustomer']
)

@router.post('/{id}', status_code=status.HTTP_201_CREATED)
def create(id:int,request: schemas.MerchantCustomer, db:Session= (Depends(database.get_db))): #,current_user:schemas.UserTest=Depends(oauth2.get_current_user)):
    return merchant_customer.create(id,request,db)


@router.post('/', status_code=200, response_model=schemas.MerchantCustomerSearch)
def search(request:schemas.MerchantCustomerSearch,db:Session = Depends(database.get_db)):
    return merchant_customer.search(request,db)

@router.get('/', response_model=List[schemas.MerchantCustomer])
#def all(db:Session = Depends(database.get_db),current_user:schemas.UserTest=Depends(oauth2.get_current_user)):
def all(db:Session = Depends(database.get_db)):
    return merchant_customer.get_all(db)


@router.get('/{id}', status_code=200, response_model=schemas.MerchantCustomer)
#def show(request: schemas.Stat,db:Session = Depends(database.get_db),current_user:schemas.UserTest=Depends(oauth2.get_current_user)):
def show(id:int,db:Session = Depends(database.get_db)):
    return merchant_customer.show(id,db)


@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED, response_model=schemas.MerchantCustomerUpdate)
def update(id:int, request:schemas.MerchantCustomerUpdate, db:Session = Depends(database.get_db)): #,current_user:schemas.UserTest=Depends(oauth2.get_current_user)):
    return merchant_customer.update(id,db,request)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int, db:Session = Depends(database.get_db)): #,current_user:schemas.UserTest=Depends(oauth2.get_current_user)):
    return merchant_customer.delete(id, db)
