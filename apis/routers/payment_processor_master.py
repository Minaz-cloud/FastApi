from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from .. import schemas,database
from ..repository import payment_processor_master
from typing import List

router = APIRouter(
    prefix= '/payment_processor_master',
    tags=['PaymentProcessorMaster']
)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.PaymentProcessorMasterUpdate, db:Session= (Depends(database.get_db))): #,current_user:schemas.UserTest=Depends(oauth2.get_current_user)):
    return payment_processor_master.create(request,db)


'''@router.post('/', status_code=200, response_model=schemas.PaymentProcessorMasterSearch)
def search(request:schemas.PaymentProcessorMasterSearch,db:Session = Depends(database.get_db)):
    return payment_processor_master.search(request,db)'''

@router.get('/', response_model=List[schemas.PaymentProcessorMaster])
#def all(db:Session = Depends(database.get_db),current_user:schemas.UserTest=Depends(oauth2.get_current_user)):
def all(db:Session = Depends(database.get_db)):
    return payment_processor_master.get_all(db)


@router.get('/{id}', status_code=200, response_model=schemas.PaymentProcessorMaster)
#def show(request: schemas.Stat,db:Session = Depends(database.get_db),current_user:schemas.UserTest=Depends(oauth2.get_current_user)):
def show(id:int,db:Session = Depends(database.get_db)):
    return payment_processor_master.show(id,db)


@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED, response_model=schemas.PaymentProcessorMasterUpdate)
def update(id:int, request:schemas.PaymentProcessorMasterUpdate, db:Session = Depends(database.get_db)): #,current_user:schemas.UserTest=Depends(oauth2.get_current_user)):
    return payment_processor_master.update(id,db,request)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int, db:Session = Depends(database.get_db)): #,current_user:schemas.UserTest=Depends(oauth2.get_current_user)):
    return payment_processor_master.delete(id, db)
