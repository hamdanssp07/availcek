#install:
# pip install requests
# pip install web3

import requests
import time
from web3 import Web3
from eth_account.messages import encode_defunct

# EDIT HERE////////////////////// 1-100 privat key dinggal samain aja 

WALLETS = [
    'copy privat key',
    'copy privat key',
    'copy privat key',
]

################################

def check_rewards(address, signed_message, timestamp):
    request_body = {
        'account': address,
        'signedMessage': signed_message,
        'timestamp': timestamp,
        'type': "ETHEREUM",
    }

    try:
        response = requests.post("https://claim-api.availproject.org/check-rewards", json=request_body)
        data = response.json()
        print(f"Account {address} - Rewards:", data)
    except Exception as e:
        print(f"Error checking rewards for account {address}:", e)

def start():
    for priv in WALLETS:
        w3 = Web3(Web3.HTTPProvider("https://bsc-dataseed1.binance.org:443"))
        wallet = w3.eth.account.from_key(priv)
        address = wallet.address
        timestamp = str(int(time.time()))
        message = f"Greetings from Avail!\n\nSign this message to check your eligibility. This signature will not cost you any fees.\n\nTimestamp: {timestamp}"
        signature = wallet.sign_message(encode_defunct(text=message)).signature.hex()
        check_rewards(address, signature, timestamp)
        time.sleep(1)

start()