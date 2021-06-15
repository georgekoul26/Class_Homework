# Import dependencies
import subprocess
import json
from dotenv import load_dotenv
import os

# Load and set environment variables
load_dotenv()
mnemonic=os.getenv("mnemonic")

# Import constants.py and necessary functions from bit and web3
BTC = 'btc'
ETH = 'eth'
BTCTEST = 'btc-test'
from web3 import Web3



# Create a function called `derive_wallets`
def derive_wallets(mnemonic, coin, numderive):
    command = f"./derive -g --mnemonic={mnemonic} --coin={coin} --numderive={numderive} --format=json"
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()
    return json.loads(output)

# Create a dictionary object called coins to store the output from `derive_wallets`.
coins = {"BTCTEST" : derive_wallets(mnemonic, BTCTEST, 3),
'ETH' : derive_wallets(mnemonic, ETH, 3)}
# Create a function called `priv_key_to_account` that converts privkey strings to account objects.
def priv_key_to_account(coin, priv_key):
    if coin == 'eth':
        return web3.eth.accounts.privateKeyToAccount(priv_key)
    if coin == 'btc-test':
        return bit.PrivateKeyTestenet(priv_key)


# Create a function called `create_tx` that creates an unsigned transaction appropriate metadata.
def create_tx(coin, account, to, amount):
    if coin == 'eth':
        gasEstimate = w3.eth.estimateGas({'from': account, 'to': to, 'value': amount})
        return{
            'from':account.address,
            'to': to,
            'value': amount,
            'gasPrice': w3.eth.gasPrice,
            'gas': gasEstimate,
            'nonce': w3.eth.getTransactionCount(account.address)
        }
    if coin == 'btc-test':
        return PrivateKeyTestent.prepare_transaction(account.address,[(to, amount, 'btc')])

# Create a function called `send_tx` that calls `create_tx`, signs and sends the transaction.
def send_tx(coin, account, to, amount):
    tx = create_tx(account, to, amount)
    signed_tx = account.sign_transaction(tx)
    if coin == 'eth':
        result = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    if coin == 'btc-test':
        result = NetworkAPI.broadcast_tx_testnet(signed_tx)


