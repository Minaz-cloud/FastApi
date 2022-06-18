from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from .. import models,schemas
import datetime


def create(request:schemas.PaymentProcessorMasterUpdate,db:Session):
    payment_processor = models.PaymentProcessorMaster(payment_processor_name=request.payment_processor_name,
                                                      flat_amount=request.flat_amount,
                                                      percentage = request.percentage,
                                                      status=request.status,
                                                      created_at= datetime.datetime.now(),
                                                      updated_at = datetime.datetime.now())
    db.add(payment_processor)
    db.commit()
    db.refresh(payment_processor)
    return payment_processor


def get_all(db:Session):
    payment_processor = db.query(models.PaymentProcessorMaster).all()
    return payment_processor


def search(request:schemas.PaymentProcessorMasterSearch,db:Session):

    processor_name = request.payment_processor_name
    processor_status = request.status

    if processor_name and processor_status:
        payment_processor = db.query(models.PaymentProcessorMaster).filter(models.PaymentProcessorMaster.payment_processor_title == processor_name and
                                                        models.PaymentProcessorMaster.status == processor_status).first()
    elif processor_name:
        payment_processor = db.query(models.PaymentProcessorMaster).filter(models.PaymentProcessorMaster.payment_processor_title == processor_name).first()
    elif processor_status:
        payment_processor = db.query(models.PaymentProcessorMaster).filter(models.PaymentProcessorMaster.status == processor_status).first()
    if not payment_processor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Data not found")
    return payment_processor

def show(id:int, db:Session):
    payment_processor = db.query(models.PaymentProcessorMaster).filter(models.PaymentProcessorMaster.payment_processor_id == id).first()
    if not payment_processor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Payment processor with id {id} not available")
    return payment_processor


def update(id:int,db:Session, request:schemas.PaymentProcessorMasterUpdate):
    payment_processor = db.query(models.PaymentProcessorMaster).filter(models.PaymentProcessorMaster.payment_processor_id == id)
    if not payment_processor.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Payment processor with id {id} not found')

    payment_processor.update(request.dict())
    db.commit()
    db.refresh(payment_processor)
    return request.dict()


def delete(id:int,db:Session):
    payment_processor = db.query(models.PaymentProcessorMaster).filter(models.PaymentProcessorMaster.payment_processor_id == id)
    if not payment_processor.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Payment processor with id {id} not found')
    payment_processor.delete(synchronize_session=False)
    db.commit()
    db.refresh(payment_processor)
    return {
        "Status": "Success",
        "Message": "Record deleted successfully."
    }