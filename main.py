import time
from req_lib import Message
import os

api_key = os.environ.get('test_binance_api')
api_secret = os.environ.get('test_binance_secret')


if __name__ == "__main__":
    
    msg = Message("https://testnet.binance.vision/api", api_key, api_secret)
    result = msg.get_accountInfo()
    print(result)