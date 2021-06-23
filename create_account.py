from  get_client import client
from hedera import (
	PrivateKey,
	AccountCreateTransaction,
	Hbar,
	AccountBalanceQuery
	)

class HederaAccount:

	def __init__(self, *args, **kwargs):

		self.private = PrivateKey.generate()
		self.public = self.private.getPublicKey()

		tran = AccountCreateTransaction()

		resp = tran.setKey(self.public).setInitialBalance(Hbar.fromTinybars(1000)).execute(client)

		self.receipt = resp.getReceipt(client)


	def create_new_account(self):

		acc_id = self.receipt.accountId

		balance = AccountBalanceQuery().setAccountId(acc_id).execute(client)

		balance_text = balance.hbars.toString()

		print(acc_id.toString())
		print(balance_text)



