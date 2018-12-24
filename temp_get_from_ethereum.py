# https://hackernoon.com/ethereum-smart-contracts-in-python-a-comprehensive-ish-guide-771b03990988
import time
from web3 import Web3, HTTPProvider
from web3.auto.infura import w3 as Web3_auto

import requests
import json


# from web3.eth.abi import decodeParameter
def load_file(fname):
    with open(fname, 'r') as f:
        text = f.read(-1).strip()
    return text
# contract_address     = load_file('ethereum/contract_address.txt')
# wallet_private_key   = load_file('ethereum/private_key_ropsten.txt')
# wallet_address       = load_file('ethereum/wallet_address.txt')
# infura_url           = "https://ropsten.infura.io/v3/f151bf7bdd2e4791957f52449abb0f9b"
contract_address = Web3.toChecksumAddress(contract_address.lower())
# wallet_address = Web3.toChecksumAddress(wallet_address.lower())


def decode_response(response):
    text = json.loads(response.text)
    return codecs.decode(my_rstrip(text['result'][2:]), 'hex').decode('ascii')

def my_rstrip(text):
    for _ in range(100):
        if text[-2:] == '00':
            text = text[:-2]
    return text

def enc_len(x):
    h = str(hex(x)).lstrip('0x')
    return ('0' * (2 - len(h)) + h).encode('ascii')

enc_func = 'a2e0bcfd'
keyword = 'keyword keyword keyword keyword'
len(keyword)
enc_name = (enc_len(len(keyword)) + codecs.encode(keyword.encode('ascii'), 'hex')).decode('ascii')
enc_name += '0' * (66 - len(enc_name))
len(enc_name)
js = """{"jsonrpc":"2.0","id":4,"method":"eth_call",
           "params":[{"to":"%s","data":"0x%s000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000000000000000%s"},"latest"]}"""  % (contract_address.lower(), enc_func, enc_name)

response = requests.post("https://ropsten.infura.io/", data = js)#json.dumps(payload))
decode_response(response)






# text = text['result'][2:]
#
# w3 = Web3_auto.HTTPProvider(infura_url)
# # dir(w3)
# # #WEB3_PROVIDER_URI = ""
# dir(w3)
# dir(Web3)
# w3.isConnected()
# Web3.eth.getTransactionCount(wallet_address)
# Web3.eth.enable_unaudited_features()
#
# from ethereum.contract_abi import abi
# import eth_abi
# dir(eth_abi)
# eth_abi.is_encodable(str)
# eth_abi.encode_single(typ=str, arg='keyword')
#
# Web3.eth.abi
#
#
#
# # response= {"jsonrpc":"2.0","id":2,
# #  "result":}
# to_decode = b"0x6b656b6f76000000000000000000000000000000000000000000000000000000"
#
# kek = eth_abi.decode_single('(bytes32,bytes32,uint256)', to_decode)
# kek
#
# kek = eth_abi.decode_single('bytes32', to_decode)
#
# kek.decode('utf-8').rstrip("0").encode('utf-8').hex()
# import codecs
# kek.rstrip(b"0")
# a = b'6b656b65'
# a = b'0x44843e43a43e43b4304342d63686f636f6c61746500000000000000000000000'
# a
# len(a)
# codecs.decode(a[2:], 'hex')
# b = codecs.decode(a[2:], 'hex')
# b
#
# b'\\x17FP'.decode('utf-8')
#
# a[2:]
# codecs.decode(kek[2:].replace(b'00', b''), 'hex').decode('ascii')
# str.fromhex()
# codecs.decode(a[2:], 'hex').replace(r'\x00', b'').decode('utf-8')
# kek.rstrip(b"00").decode('hex')
# bytes.fromhex()
# eth_abi.decode_abi(['bytes32,bytes32,uint256'], to_decode)
# response
#
# dir(w3)
# contract = Web3_auto.eth.contract(address = contract_address, abi = abi)
# dir(contract)
# contract.abi
# dir(contract.interface)
# _ , get_ad = contract.all_functions()
# #contract.functions.get_ad_title('keyword').call({'key': 'keyword'})
#
#
#
# get_ad = get_ad('keyword')
# get_ad.transact()
# get_ad = get_ad({'keyword': 'kek'})
# get_ad.transact()
# get_ad.call(keyword='kek')
# dir(get_ad).transact()
# #.call({'keyword': 'kek'})
#
# #dir(contract.functions.get_ad)
# call_dict = {
# 	"key": "keyword"
# }
# a = contract.functions.get_ad('keyword')
# a.arguments = call_dict
# a.call("keyword")
# dir(a)

get_ad.call({'kek': 'kek'})
dir(Web3.eth.call())

tx_hash = get_ad('Nihao').transact()


kek = contract.functions.get_ad('keyword').call({'key': ['keyword']})


a.arguments