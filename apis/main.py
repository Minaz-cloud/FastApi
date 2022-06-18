from fastapi import FastAPI
from . import models
from . database import engine
from . routers import bankmaster, merchant, merchantpricing,merchant_customer,payment_processor_master,merchant_setting

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(bankmaster.router)
app.include_router(merchant.router)
app.include_router(merchantpricing.router)
app.include_router(merchant_customer.router)
app.include_router(payment_processor_master.router)
app.include_router(merchant_setting.router)
app.include_router(merchant_setting.router)