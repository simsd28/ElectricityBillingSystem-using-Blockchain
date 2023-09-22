import json
from web3 import Web3
import pprint

web3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
from web3.middleware import geth_poa_middleware
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

web3.eth.defaultAccount = web3.eth.accounts[0]
abi = json.loads('[{"inputs": [{"internalType": "uint256","name": "num","type": "uint256"}],"name": "store","outputs": [],"stateMutability": "nonpayable","type": "function"},{"inputs": [],"name": "retrieve","outputs": [{"internalType": "uint256","name": "","type": "uint256"}],"stateMutability": "view","type": "function"}]')
bytecode = '608060405234801561001057600080fd5b5061012f806100206000396000f3fe6080604052348015600f57600080fd5b506004361060325760003560e01c80632e64cec11460375780636057361d146051575b600080fd5b603d6069565b6040516048919060c2565b60405180910390f35b6067600480360381019060639190608f565b6072565b005b60008054905090565b8060008190555050565b60008135905060898160e5565b92915050565b60006020828403121560a057600080fd5b600060ac84828501607c565b91505092915050565b60bc8160db565b82525050565b600060208201905060d5600083018460b5565b92915050565b6000819050919050565b60ec8160db565b811460f657600080fd5b5056fea264697066735822122062db17618d746a1967495ede611efc2c1e881cb29cbd6b40b23bd35a720c134c64736f6c63430008010033'
contract_address= '0xBF153F858758988C3F757df8CA9d551f240e8E14'

contract = web3.eth.contract(abi=abi, bytecode=bytecode, address=contract_address)

num = input ("Enter value:")
tx_hash = contract.functions.store(num).transact()
receipt = web3.eth.waitForTransactionReceipt(tx_hash)
print("Transaction receipt mined:")
pprint.pprint(dict(receipt))
print("\nWas transaction successful?")
pprint.pprint(receipt["status"])