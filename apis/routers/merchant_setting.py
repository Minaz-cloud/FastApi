from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from .. import schemas,database
from ..repository import merchant_setting
from typing import List

router = APIRouter(
    prefix= '/merchant_settings',
    tags=['MerchantSettings']
)

@router.post('/{id}', status_code=status.HTTP_201_CREATED,operation_id="post with id")
def create(id:int,request: schemas.MerchantSetting, db:Session= (Depends(database.get_db))): #,current_user:schemas.UserTest=Depends(oauth2.get_current_user)):
    return merchant_setting.create(id,request,db)

'''
@router.post('/', status_code=200, response_model=schemas.MerchantSetting)
def search(request:schemas.MerchantSetting,db:Session = Depends(database.get_db)):
    return merchant_setting.search(request,db)
'''


@router.get('/{id}', status_code=200, response_model=schemas.MerchantSetting,operation_id="get with id")
#def show(request: schemas.Stat,db:Session = Depends(database.get_db),current_user:schemas.UserTest=Depends(oauth2.get_current_user)):
def show(id:int,db:Session = Depends(database.get_db)):
    return merchant_setting.show(id,db)


@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED, response_model=schemas.MerchantSettingUpdate,operation_id="put with id")
def update(id:int, request:schemas.MerchantSettingUpdate, db:Session = Depends(database.get_db)): #,current_user:schemas.UserTest=Depends(oauth2.get_current_user)):
    return merchant_setting.update(id,db,request)


@router.delete('/{id}',operation_id="delete by id")#, status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int, db:Session = Depends(database.get_db)): #,current_user:schemas.UserTest=Depends(oauth2.get_current_user)):
    return merchant_setting.delete(id, db)
