import decimal

from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class BankBase(BaseModel):
    bank_id:int
    bank_code : str
    bank_name : str
    status : int
    created_at : datetime
    updated_at : datetime


class Bank(BankBase):
    class Config():
        orm_mode = True


class BankBaseUpdate(BaseModel):
    bank_code: str
    bank_name: str
    status: int
    class Config():
        orm_mode = True


class Merchant(BaseModel):
    paynet_merchant_id : int
    user_id : int
    security_deposit : decimal.Decimal
    processor_merchant_id : int
    merchant_balance : decimal.Decimal
    payin_committed_volume :int
    payout_committed_volume :int
    status : int
    created_at : datetime
    updated_at : datetime


class MerchantBase(Merchant):
    class Config():
        orm_mode = True


class MerchantUpdate(BaseModel):

    security_deposit: decimal.Decimal
    merchant_balance: decimal.Decimal
    payin_committed_volume: int
    payout_committed_volume: int
    status: int
    class Config():
        orm_mode = True


class MerchantPricing(BaseModel):
    merchant_pricing_id : int
    paynet_merchant_id : int
    payin_flat_amount : dict={
        "CC":'',
        "DC":'',
        "NB":'',
        "UPI":''
    }
    payin_percentage : dict={
        "CC": '',
        "DC": '',
        "NB": '',
        "UPI": ''
    }
    payout_flat_amount : decimal.Decimal
    payout_percentage : str
    created_at : datetime
    updated_at : datetime
    class Config():
        orm_mode = True


class MerchantPricingCrud(BaseModel):
    payin_flat_amount: dict = {
        "CC": '',
        "DC": '',
        "NB": '',
        "UPI": ''
    }
    payin_percentage: dict = {
        "CC": '',
        "DC": '',
        "NB": '',
        "UPI": ''
    }
    payout_flat_amount: decimal.Decimal
    payout_percentage: str
    class Config():
        orm_mode = True


class MerchantCustomer(BaseModel):
    merchant_customer_id :int
    paynet_merchant_id :int
    customer_name :str
    customer_email :str
    customer_contact_no :str
    address1 :str
    address2 :str
    city :str
    state :str
    pincode :int
    gstin :str
    created_at: datetime
    updated_at: datetime


class MerchantCustomerUpdate(BaseModel):
    customer_name: str
    customer_email: str
    customer_contact_no: str
    address1: str
    address2: str
    city: str
    state: str
    pincode: int
    gstin: str
    class Config():
        orm_mode = True


class MerchantCustomerSearch(BaseModel):
    customer_name: Optional[str] = None
    customer_email: Optional[str] = None
    customer_contact_no: Optional[str] = None


class PaymentProcessorMaster(BaseModel):
    payment_processor_id : int
    payment_processor_name :str
    flat_amount :decimal.Decimal
    percentage :str
    status :int
    created_at: datetime
    updated_at: datetime
    class Config():
        orm_mode = True


class PaymentProcessorMasterUpdate(BaseModel):
    payment_processor_name: str
    flat_amount: decimal.Decimal
    percentage: str
    status: int
    class Config():
        orm_mode = True


class PaymentProcessorMasterSearch(BaseModel):
    payment_processor_name: Optional[str]
    status: Optional[int]


class MerchantSetting(BaseModel):
    merchant_setting_id :int
    paynet_merchant_id :int
    payin_webhook_url :str
    payout_webhook_url :str
    merchant_secret_key :str
    merchant_appid :str
    ip_address :str
    status :int
    create_at :datetime
    updated_at :datetime


class MerchantSettingUpdate(BaseModel):
    payin_webhook_url: str
    payout_webhook_url: str
    merchant_secret_key: str
    merchant_appid: str
    ip_address: str
    status: int
    class Config():
        orm_mode = True


class MerchantLimit(BaseModel):
    merchant_limit_id :int
    paynet_merchant_id :int
    daily_payin_volume_limit :int
    daily_payin_transaction_limit :int
    daily_payout_volume_limit :int
    daily_payout_transaction_limit :int
    daily_payin_withdrawal :int
    daily_payout_withdrawal :int
    created_at :datetime
    updated_at :datetime
    class Config():
        orm_mode = True


class MerchantLimitCurd(BaseModel):
    daily_payin_volume_limit: int
    daily_payin_transaction_limit: int
    daily_payout_volume_limit: int
    daily_payout_transaction_limit: int
    daily_payin_withdrawal: int
    daily_payout_withdrawal: int
    class Config():
        orm_mode = True