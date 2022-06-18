from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from .. import models,schemas
import datetime


def create(request:schemas.BankBaseUpdate,db:Session):
    bank = models.BankMaster(bank_code=request.bank_code,
                             bank_name=request.bank_name,
                             status= request.status,
                             created_at= datetime.datetime.now(),
                             updated_at = datetime.datetime.now())
    db.add(bank)
    db.commit()
    db.refresh(bank)
    return bank


def get_all(db:Session):
    banks = db.query(models.BankMaster).all()
    return banks


def show(id:int, db:Session):
    bank = db.query(models.BankMaster).filter(models.BankMaster.bank_id == id).first()
    if not bank:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Bank with the {id} not available")
    return bank


def update(id:int,request:schemas.BankBaseUpdate,db:Session):
    bank = db.query(models.BankMaster).filter(models.BankMaster.bank_id == id)
    if not bank.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Bank with id {id} not found')

    bank.update(request.dict())
    db.commit()
    # db.refresh(bank)
    msg = {
        "Status": "Success",
        "data": request.dict()
    }
    return msg


def delete(id:int,db:Session):
    bank = db.query(models.BankMaster).filter(models.BankMaster.bank_id == id)
    if not bank.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Bank with id {id} not found')
    bank.delete()
    db.commit()
    dic = {"Status": "Success",
           "Message": "Records deleted successfully.",
           "data": {"Bank_id": id}
           }
    return dic
