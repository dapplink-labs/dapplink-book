import os
from web3 import Web3
from dotenv import load_dotenv
import json
import time
from datetime import datetime

# Load environment variables
load_dotenv()

# Initialize Web3
w3 = Web3(Web3.HTTPProvider(os.getenv('ETHEREUM_RPC_URL', 'https://mainnet.infura.io/v3/YOUR-PROJECT-ID')))

# Known whale addresses (example addresses - replace with actual addresses)
WHALE_ADDRESSES = {
    'CZ': '0x28C6c06298d514Db089934071355E5743bf21d60',  # Binance hot wallet
    'Sun': '0x3DdfA8eC3052539b6C0909B96e9B0DfA0D5B4E0',  # Example address
    'Bao': '0x28C6c06298d514Db089934071355E5743bf21d60',  # Example address
    'BlackRock': '0x28C6c06298d514Db089934071355E5743bf21d60',  # Example address
}

# Minimum balance threshold in USD (10 million)
MIN_BALANCE_USD = 10_000_000

def get_eth_balance(address):
    """Get ETH balance for an address"""
    balance_wei = w3.eth.get_balance(address)
    balance_eth = w3.from_wei(balance_wei, 'ether')
    return balance_eth

def get_token_balance(token_address, wallet_address):
    """Get ERC20 token balance for an address"""
    # ERC20 ABI for balanceOf
    abi = json.loads('[{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"type":"function"}]')
    contract = w3.eth.contract(address=token_address, abi=abi)
    balance = contract.functions.balanceOf(wallet_address).call()
    return balance

def monitor_transactions():
    """Monitor transactions for whale addresses"""
    print("Starting whale transaction monitoring...")
    
    while True:
        for name, address in WHALE_ADDRESSES.items():
            try:
                # Get latest block
                latest_block = w3.eth.block_number
                
                # Get transactions for the address
                balance = get_eth_balance(address)
                print(f"{name}'s ETH Balance: {balance} ETH")
                
                # Here you would add logic to:
                # 1. Check token balances
                # 2. Monitor incoming/outgoing transactions
                # 3. Calculate USD value
                # 4. Alert on significant movements
                
                time.sleep(1)  # Avoid rate limiting
                
            except Exception as e:
                print(f"Error monitoring {name}'s address: {str(e)}")
                continue

def main():
    if not w3.is_connected():
        print("Failed to connect to Ethereum network")
        return
    
    print("Connected to Ethereum network")
    monitor_transactions()

if __name__ == "__main__":
    main() 