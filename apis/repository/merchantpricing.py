import datetime

from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from .. import models,schemas


payin_flat_amount={
    "type":"object",
    "properties":{
        "CC":{"type":"string"},
        "DC":{"type":"string"},
        "NB":{"type":"string"},
        "UPI":{"type":"string"},
    },
}
payin_percentage={
    "type":"object",
    "properties":{
        "CC":{"type":"string"},
        "DC":{"type":"string"},
        "NB":{"type":"string"},
        "UPI":{"type":"string"},
    },
}


def create(id:int, db:Session, request:schemas.MerchantPricingCrud):

    merchant_pricing = models.MerchantPricing(paynet_merchant_id=id,
                                              payin_flat_amount=request.payin_flat_amount,
                                              payin_percentage=request.payin_percentage,
                                              payout_flat_amount = request.payout_flat_amount,
                                              payout_percentage=request.payout_percentage,
                                              created_at = datetime.datetime.now(),
                                              updated_at = datetime.datetime.now())
    db.add(merchant_pricing)
    db.commit()
    db.refresh(merchant_pricing)
    return merchant_pricing


def show(id:int, db:Session):
    merchant_pricing = db.query(models.MerchantPricing).filter(models.MerchantPricing.paynet_merchant_id == id).first()
    if not merchant_pricing:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Merchant with id {id} not available")
    return merchant_pricing


def update(id:int,db:Session, request:schemas.MerchantPricingCrud):
    merchant_pricing = db.query(models.MerchantPricing).filter(models.MerchantPricing.paynet_merchant_id == id)
    if not merchant_pricing.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Merchant with id {id} not found')
    merchant_pricing.update(request.dict())
    db.commit()
    msg = {
              "Status": "Success",
              "data":request.dict()
          }
    return msg


def delete(id:int,db:Session):
    merchant_pricing = db.query(models.MerchantPricing).filter(models.MerchantPricing.paynet_merchant_id == id)
    if not merchant_pricing.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Merchant with {id} not found')
    merchant_pricing.delete(synchronize_session=False)
    db.commit()
    # db.refresh(merchant_pricing)
    dic= {"Status": "Success",
          "Message": "Records deleted successfully.",
          "data" : {"Merchant_id" : id}
          }
    return dic
