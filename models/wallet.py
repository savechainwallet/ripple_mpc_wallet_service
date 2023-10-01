from peewee import *
import models

class RippleWallet(models.BaseModel):
    address = CharField()
    user_id = CharField()
    master_share_b = CharField()
    signer_one_account = CharField()
    third_signing_public_key = CharField()
    third_signing_private_key = CharField()
    created_at = DateTimeField()
    updated_at = DateTimeField()

   


    



