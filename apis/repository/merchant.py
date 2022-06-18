from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from .. import models,schemas


def get_all(db:Session):
    merchant = db.query(models.Merchant).all()
    return merchant


def show(id:int, db:Session):
    merchant = db.query(models.Merchant).filter(models.Merchant.paynet_merchant_id == id).first()
    if not merchant:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Merchant with id {id} not available")
    return merchant


def update(id:int,db:Session, request:schemas.MerchantUpdate):
    merchant = db.query(models.Merchant).filter(models.Merchant.paynet_merchant_id == id)
    if not merchant.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Merchant with id {id} not found')

    merchant.update(request.dict())
    db.commit()
    return request.dict()


def delete(id:int,db:Session):
    merchant = db.query(models.Merchant).filter(models.Merchant.paynet_merchant_id == id)
    if not merchant.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Merchant with id {id} not found')
    merchant.delete(synchronize_session=False)
    db.commit()
    # return "done"
    return {
        "Status": "Success",
        "Message": "Record deleted successfully."
    }