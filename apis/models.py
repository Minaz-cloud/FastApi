from . database import Base
from sqlalchemy import Column,Integer,String,DateTime,Numeric,BigInteger,SmallInteger,JSON


class BankMaster(Base):

    __tablename__: str = "bank_master"
    bank_id = Column(Integer,primary_key=True, unique=True)
    bank_code = Column(String(45))
    bank_name = Column(String(45))
    status = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class Merchant(Base):

    __tablename__: str = "merchant"
    paynet_merchant_id = Column(Integer,primary_key=True, unique = True)
    user_id = Column(Integer)
    security_deposit = Column(Numeric(11,3))
    processor_merchant_id = Column(Integer)
    merchant_balance = Column(Numeric(11,3))
    payin_committed_volume = Column(BigInteger)
    payout_committed_volume = Column(BigInteger)
    status = Column(SmallInteger)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class MerchantPricing(Base):

    __tablename__ :str = "merchant_pricing"
    merchant_pricing_id = Column(Integer,primary_key=True, unique = True)
    paynet_merchant_id = Column(Integer)
    payin_flat_amount=Column(JSON)
    payin_percentage=Column(JSON)
    payout_flat_amount= Column(Numeric(3,2))
    payout_percentage= Column(String(255))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

class MerchantCustomer(Base):

    __tablename__:str = "merchant_customer"
    merchant_customer_id = Column(Integer,primary_key=True, unique = True)
    paynet_merchant_id = Column(Integer)
    customer_name = Column(String(255))
    customer_email = Column(String(255))
    customer_contact_no = Column(String(100))
    address1 = Column(String(255))
    address2 = Column(String(255))
    city = Column(String(255))
    state = Column(String(255))
    pincode = Column(String(255))
    gstin = Column(String(255))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class PaymentProcessorMaster(Base):

    __tablename__: str = "payment_processor_master"
    payment_processor_id= Column(Integer,primary_key=True, unique = True)
    payment_processor_name = Column(String(255))
    status = Column(Integer)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)


class MerchatSettings(Base):

    __tablename__ :str = "merchant_setting"
    merchant_setting_id = Column(Integer,primary_key=True, unique = True)
    paynet_merchant_id = Column(Integer)
    payin_webhook_url = Column(String(255))
    payout_webhook_url = Column(String(255))
    merchant_secret_key = Column(String(255))
    merchant_appid = Column(String(255))
    ip_address = Column(String(255))
    status = Column(Integer)
    create_at = Column(DateTime)
    updated_at = Column(DateTime)


class MerchantLimit(Base):
    __tablename__ :str = "merchant_limit"
    merchant_limit_id = Column(Integer,primary_key=True, unique = True)
    paynet_merchant_id = Column(Integer)
    daily_payin_volume_limit= Column(BigInteger)
    daily_payin_transaction_limit= Column(BigInteger)
    daily_payout_volume_limit= Column(BigInteger)
    daily_payout_transaction_limit= Column(BigInteger)
    daily_payin_withdrawal= Column(BigInteger)
    daily_payout_withdrawal= Column(BigInteger)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
