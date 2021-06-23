import os
from hedera import Client, AccountId, PrivateKey

OPERATOR_ID = AccountId.fromString(os.environ["OPERATOR_ID"])
OPERATOR_KEY = PrivateKey.fromString(os.environ["OPERATOR_KEY"])

client = Client.forTestnet()
client.setOperator(OPERATOR_ID, OPERATOR_KEY)