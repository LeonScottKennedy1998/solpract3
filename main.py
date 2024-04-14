from web3 import Web3
from web3.middleware import geth_poa_middleware
from account_info import abi,contract_address

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
contract = w3.eth.contract(address=contract_address, abi=abi)

print(contract.address)
print(w3.eth.get_balance("0xFB896c5495373AF434C0C1ed30Bf36C504fc327A"))
print(w3.eth.get_balance("0xff7Aa4EE76f50F64D6F7604368dDbfC901e8Fde7"))
print(w3.eth.get_balance("0xE01Ef9D0973823a108e26F3c3c45233F6E705590"))
print(w3.eth.get_balance("0x2A4e0a4eFA8335f97a987c3eE1ae1c17bbfD35d9"))
print(w3.eth.get_balance("0xe1108fe7c8dB89358be60C43c194Eca2A58E1750"))
