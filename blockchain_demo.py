from blockchain import Blockchain, Transaction

def demo():
    blockchain = Blockchain()

    blockchain.add_transaction(Transaction("Alice", "Bob", 50))
    blockchain.add_transaction(Transaction("Bob", "Charlie", 20))
    blockchain.mine_block()

    for block in blockchain.chain:
        print(f"Block Hash: {block.hash}")
        print(f"Merkle Root: {block.merkle_root}")
        print(f"Transactions: {[str(tx) for tx in block.transactions]}")
        print("-" * 40)

    print(f"Blockchain valid: {blockchain.validate_blockchain()}")

if __name__ == "__main__":
    demo()
