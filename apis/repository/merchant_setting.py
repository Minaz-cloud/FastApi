from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from .. import models,schemas
import datetime


def create(id:int, db:Session, request:schemas.MerchantSetting):
    merchant_setting = models.MerchatSettings(paynet_merchant_id=id,
                                              payin_webhook_url= request.payin_webhook_url,
                                              payout_webhook_url = request.payout_webhook_url,
                                              merchant_secret_key = request.merchant_secret_key,
                                              merchant_appid = request.merchant_appid,
                                              ip_address = request.ip_address,
                                              status=request.status,
                                              created_at= datetime.datetime.now(),
                                              updated_at = datetime.datetime.now())
    db.add(merchant_setting)
    db.commit()
    db.refresh(merchant_setting)
    return merchant_setting


def get_all(db:Session):
    merchant_setting = db.query(models.MerchatSettings).all()
    return merchant_setting

'''
def search(request:schemas.PaymentProcessorMasterSearch,db:Session):

    processor_title = request.payment_processor_title
    processor_status = request.status

    if processor_title and processor_status:
        payment_processor = db.query(models.PaymentProcessorMaster).filter(models.PaymentProcessorMaster.payment_processor_title == processor_title and
                                                        models.PaymentProcessorMaster.status == processor_status).first()
    elif processor_title:
        payment_processor = db.query(models.PaymentProcessorMaster).filter(models.PaymentProcessorMaster.payment_processor_title == processor_title).first()
    elif processor_status:
        payment_processor = db.query(models.PaymentProcessorMaster).filter(models.PaymentProcessorMaster.status == processor_status).first()
    if not payment_processor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Data not found")
    return payment_processor
'''
def show(id:int, db:Session):
    merchant_setting = db.query(models.MerchatSettings).filter(models.MerchatSettings.paynet_merchant_id == id).first()
    if not merchant_setting:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Merchant  with id {id} not available")
    return merchant_setting


def update(id:int,db:Session, request:schemas.MerchantSettingUpdate):
    merchant_setting = db.query(models.MerchatSettings).filter(models.MerchatSettings.paynet_merchant_id == id)
    if not merchant_setting.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Merchant with id {id} not found')

    merchant_setting.update(request.dict())
    db.commit()
    db.refresh(merchant_setting)
    return request.dict()


def delete(id:int,db:Session):
    merchant_setting = db.query(models.MerchatSettings).filter(models.MerchatSettings.paynet_merchant_id == id)
    if not merchant_setting.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Merchant with id {id} not found')
    merchant_setting.delete()
    db.commit()

    return {
        "Status": "Success",
        "Message": "Record deleted successfully."
    }