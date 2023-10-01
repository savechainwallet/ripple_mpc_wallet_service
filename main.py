from fastapi import FastAPI
from peewee import SqliteDatabase
from xrpl.clients import JsonRpcClient
from pydantic import BaseModel
from usecases import CreateWalletUsecase
import models


JSON_RPC_URL = "https://s.altnet.rippletest.net:51234/"
client = JsonRpcClient(JSON_RPC_URL)
app = FastAPI()

db =  SqliteDatabase(':memory:')
models.database_proxy.initialize(db)
db.create_tables([models.RippleWallet])

class CreateWalletRequest(BaseModel):
    user_id: str
    address: str 
    share_b: str
    signer_one_account:str

@app.post("/wallet")
async def create_wallet(req: CreateWalletRequest):
    us = CreateWalletUsecase(user_id= req.user_id, address=req.address,share_b= req.share_b,signer_one_account=req.signer_one_account,db=db, client=client )
    resp = us.run()
    return resp