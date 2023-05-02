import hashlib
import time
import random
from termcolor import colored

max_nonce = 2 ** 64
difficulty = 4

version = 1
previous_block_hash = "00000000000000000006a78e7de1d304b1d2f0c5bca617b0e8c88d2399be5d5"
merkle_root = "8c8d0bdecb58ab3b61e46e8f76f0f9b3d3c3bfe0128c0d4adbbf57850c13c688"
timestamp = int(time.time())
bits = 0x1b0404cb
nonce = 0
total_bitcoin = 0

while True:
    block_header = f"{version}{previous_block_hash}{merkle_root}{timestamp}{bits}{nonce}".encode('utf-8')
    hash = hashlib.sha256(hashlib.sha256(block_header).digest()).hexdigest()
    if hash.startswith('0' * difficulty):
        block_reward = random.uniform(0.00000000001, 0.00000000003)
        total_bitcoin += block_reward
        total_bitcoin_str = "{:.11f}".format(total_bitcoin)
        print(colored(f"|Hash: {hash} | Nonce: {str(nonce)[:5].rjust(5)} | BTC: {total_bitcoin_str} |", "green"))
        previous_block_hash = hash
        nonce = 0
        time.sleep(1)
        if int(total_bitcoin * 100000000) % 100000 == 0:
            difficulty += 1
    else:
        nonce += 1
        if nonce >= max_nonce:
            bits += 1
            nonce = 0
