# https://hackernoon.com/ethereum-smart-contracts-in-python-a-comprehensive-ish-guide-771b03990988
import time
#from web3 import Web3, HTTPProvider
from web3.auto.infura import w3 as Web3

def load_file(fname):
    with open(fname, 'r') as f:
        text = f.read(-1).strip()
    return text

contract_address     = load_file('ethereum/contract_address.txt')
wallet_private_key   = load_file('ethereum/private_key_ropsten.txt')
wallet_address       = load_file('ethereum/wallet_address.txt')
infura_url           = "https://ropsten.infura.io/v3/f151bf7bdd2e4791957f52449abb0f9b"
contract_address = Web3.toChecksumAddress(contract_address.lower())
wallet_address = Web3.toChecksumAddress(wallet_address.lower())

w3 = Web3.HTTPProvider(infura_url)
# dir(w3)
# #WEB3_PROVIDER_URI = ""

w3.isConnected()
Web3.eth.getTransactionCount(wallet_address)
Web3.eth.enable_unaudited_features()

from ethereum.contract_abi import abi

contract = Web3.eth.contract(address = contract_address, abi = abi)
#dir(contract.functions.get_ad)
call_dict = {
	"key": "keyword"
}
a = contract.functions.get_ad('keyword')
a.arguments = call_dict
a.call("keyword")
dir(a)

_ , get_ad = contract.all_functions()
get_ad.call({'kek': 'kek'})
dir(Web3.eth.call())

tx_hash = get_ad('Nihao').transact()


kek = contract.functions.get_ad('keyword').call({'key': ['keyword']})


a.arguments