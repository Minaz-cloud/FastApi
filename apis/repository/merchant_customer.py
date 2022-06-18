from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from .. import models,schemas
import datetime


def create(id:int, db:Session, request:schemas.MerchantCustomer):
    merchant_customer = models.MerchantCustomer(paynet_merchant_id=id, customer_name=request.customer_name,
                                                customer_email=request.customer_email,
                                                customer_contact_no = request.customer_contact_no,
                                                address1=request.address1,
                                                address2 = request.address2,
                                                city = request.city,state=request.state,pincode=request.pincode,
                                                gstin=request.gstin, created_at= datetime.datetime.now(),
                                                updated_at = datetime.datetime.now())
    db.add(merchant_customer)
    db.commit()
    db.refresh(merchant_customer)
    return merchant_customer


def get_all(db:Session):
    merchant_customer = db.query(models.MerchantCustomer).all()
    return merchant_customer


def search(request:schemas.MerchantCustomerSearch,db:Session):

    customer_name = request.customer_name
    customer_email = request.customer_email
    customer_contact_no = request.customer_contact_no

    if customer_name and customer_email and customer_contact_no:
        cust = db.query(models.MerchantCustomer).filter(models.MerchantCustomer.customer_name == customer_name and
                                                        models.MerchantCustomer.customer_email == customer_email and
                                                        models.MerchantCustomer.customer_contact_no == customer_contact_no).first()
    elif customer_name and customer_email:
        cust = db.query(models.MerchantCustomer).filter(models.MerchantCustomer.customer_name == customer_name and
                                                        models.MerchantCustomer.customer_email == customer_email).first()
    elif customer_name and customer_contact_no:
        cust = db.query(models.MerchantCustomer).filter(models.MerchantCustomer.customer_name == customer_name and
                                                        models.MerchantCustomer.customer_contact_no == customer_contact_no).first()
    elif customer_name:
        cust = db.query(models.MerchantCustomer).filter(models.MerchantCustomer.customer_name == customer_name).first()

    elif customer_email and customer_contact_no:
        cust = db.query(models.MerchantCustomer).filter(models.MerchantCustomer.customer_email == customer_email and
                                                        models.MerchantCustomer.customer_contact_no == customer_contact_no).first()
    elif customer_email:
        cust = db.query(models.MerchantCustomer).filter(models.MerchantCustomer.customer_email == customer_email).first()
    elif customer_contact_no:
        cust = db.query(models.MerchantCustomer).filter(models.MerchantCustomer.customer_contact_no == customer_contact_no).first()
    if not cust:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Data not found")
    return cust

def show(id:int, db:Session):
    merchant_customer = db.query(models.MerchantCustomer).filter(models.MerchantCustomer.merchant_customer_id == id).first()
    if not merchant_customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Customer with id {id} not available")
    return merchant_customer


def update(id:int,db:Session, request:schemas.MerchantCustomerUpdate):
    merchant_customer = db.query(models.MerchantCustomer).filter(models.MerchantCustomer.merchant_customer_id == id)
    if not merchant_customer.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Customer with id {id} not found')

    merchant_customer.update(request.dict())
    db.commit()
    return request.dict()


def delete(id:int,db:Session):
    merchant_customer = db.query(models.MerchantCustomer).filter(models.MerchantCustomer.merchant_customer_id == id)
    if not merchant_customer.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Customer with id {id} not found')
    merchant_customer.delete(synchronize_session=False)
    db.commit()
    return {
        "Status": "Success",
        "Message": "Record deleted successfully."
    }