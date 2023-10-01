from xrpl.wallet import Wallet
from xrpl.models.transactions import SignerListSet, SignerEntry
from xrpl.transaction import autofill
from models import RippleWallet, database_proxy
import datetime

class CreateWalletUsecase:
    def __init__(self,user_id, address, share_b,signer_one_account, db, client):
        self.user_id = user_id
        self.address = address
        self.share_b = share_b
        self.signer_one_account = signer_one_account
        self.db = db
        self.client = client

    def run(self):
        # Creating ripple wallet
        w = Wallet.create()

        # Creating model 
        this_wallet = RippleWallet(address= self.address,
                                    user_id= self.user_id, 
                                    master_share_b= self.share_b,
                                    third_signing_public_key= w.public_key,
                                    third_signing_private_key=w.private_key,
                                    signer_one_account= self.signer_one_account,
                                    created_at= datetime.datetime.now(),
                                    updated_at= datetime.datetime.now()
                                    )
        this_wallet.save()

        tx = SignerListSet(account=this_wallet.address, signer_quorum= 2, signer_entries= [
            SignerEntry(account=self.signer_one_account, signer_weight=1),
            SignerEntry(account=this_wallet.third_signing_public_key, signer_weight=1)

        ])
        autofill(tx,self.client)
        return tx



        
