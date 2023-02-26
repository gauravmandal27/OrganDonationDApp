import json
from web3 import Web3, HTTPProvider
import time
# truffle development blockchain address
blockchain_address = 'http://127.0.0.1:9545'
# Client instance to interact with the blockchain
web3 = Web3(HTTPProvider(blockchain_address))
# Set the default account (so we don't need to set the "from" for every transaction call)
web3.eth.defaultAccount = web3.eth.accounts[0]

# Path to the compiled contract JSON file
compiled_contract_path = 'Student.json'
# Deployed contract address (see `migrate` command output: `contract address`)
deployed_contract_address = '0xa02CF1CF73b96B5762030951de60FFC812524c4D'

with open(compiled_contract_path) as file:
    contract_json = json.load(file)  # load contract info as JSON
    contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions

# Fetch deployed contract reference
contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)

# Call contract function (this is not persisted to the blockchain)
print("first")
msg = contract.functions.enrollStudent("1,Modi,Sunflower High School,High School,10-06-1990").transact()
tx_receipt = web3.eth.waitForTransactionReceipt(msg)
print('tx_hash: {}'.format(msg.hex()))
print("second")
print(msg)


details = contract.functions.getStudent().call()
print(details)
'''
msg = contract.functions.markVote(2,"Modi","Lotus","saleem","12345").transact()
tx_receipt = web3.eth.waitForTransactionReceipt(msg)
message = contract.functions.getCount(2).call()
print(message)
'''
