import datetime
from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from .. import models,schemas


def create(id:int, db:Session, request:schemas.MerchantLimit):

    merchant_limit = models.MerchantLimit(paynet_merchant_id=id,
                                          daily_payin_volume_limit=request.daily_payin_volume_limit,
                                          daily_payin_transaction_limit=request.daily_payin_transaction_limit,
                                          daily_payout_volume_limit = request.daily_payout_volume_limit,
                                          daily_payout_transaction_limit=request.daily_payout_transaction_limit,
                                          daily_payin_withdrawal = request.daily_payin_withdrawal,
                                          daily_payout_withdrawal = request.daily_payout_withdrawal,
                                          created_at = datetime.datetime.now(),
                                          updated_at = datetime.datetime.now())
    db.add(merchant_limit)
    db.commit()
    db.refresh(merchant_limit)
    return merchant_limit


def show(id:int, db:Session):
    merchant_limit = db.query(models.MerchantLimit).filter(models.MerchantLimit.paynet_merchant_id == id).first()
    if not merchant_limit:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Merchant with id {id} not available")
    return merchant_limit


def update(id:int,db:Session, request:schemas.MerchantLimitCurd):
    merchant_limit = db.query(models.MerchantLimit).filter(models.MerchantLimit.paynet_merchant_id == id)
    if not merchant_limit.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Merchant with id {id} not found')
    merchant_limit.update(request.dict())
    db.commit()
    return request.dict()


def delete(id:int,db:Session):
    merchant_limit = db.query(models.MerchantLimit).filter(models.MerchantLimit.paynet_merchant_id == id)
    if not merchant_limit.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Merchant with {id} not found')
    merchant_limit.delete(synchronize_session=False)
    db.commit()
    return {
        "Status": "Success",
        "Message": "Record deleted successfully."
    }